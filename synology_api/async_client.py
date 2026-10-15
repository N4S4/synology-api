"""
Async client wrapper for synology-api.

Wraps any synchronous synology-api class and makes all its methods
awaitable by offloading calls to a thread pool executor.

Usage::

    import asyncio
    from synology_api import FileStation
    from synology_api.async_client import AsyncClient

    async def main():
        fs = AsyncClient(FileStation("192.168.1.2", "5001", "admin", "pass"))
        info = await fs.get_info()
        files = await fs.list_folder("/home")

    asyncio.run(main())

Zero code duplication — all existing sync modules gain async support
automatically.  When a new method is added to ``FileStation`` (or any
other sync class) it is immediately available as ``await`` on the
wrapped instance.
"""

from __future__ import annotations

import asyncio
import functools
from typing import Any, TypeVar

T = TypeVar("T")


def _make_async_callable(
    original: Any, name: str, semaphore: asyncio.Semaphore | None = None
) -> Any:
    """
    Wrap a synchronous callable so it runs in a thread-pool executor.

    ``name`` is kept only for debug/traceback readability.

    Parameters
    ----------
    original : Any
        The synchronous callable to wrap.
    name : str
        The attribute name, used only for debug/traceback context.
    semaphore : asyncio.Semaphore, optional
        If given, caps the number of concurrent in-flight calls.  This is
        the guard against NAS session limits (e.g. the DS218+ drops
        sessions under heavy parallel load).

    Returns
    -------
    Any
        An async wrapper that, when awaited, executes ``original`` via
        ``loop.run_in_executor``.  If ``original`` is not callable it
        is returned unchanged.
    """
    if not callable(original):
        return original

    @functools.wraps(original)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Execute the wrapped callable in a thread-pool executor.

        Parameters
        ----------
        *args : Any
            Positional arguments forwarded to the original callable.
        **kwargs : Any
            Keyword arguments forwarded to the original callable.

        Returns
        -------
        Any
            The return value of the original callable.
        """
        loop = asyncio.get_running_loop()
        # functools.partial binds args/kwargs into a zero-arg callable,
        # which is what run_in_executor expects.
        task = functools.partial(original, *args, **kwargs)
        if semaphore is None:
            return await loop.run_in_executor(None, task)
        async with semaphore:
            return await loop.run_in_executor(None, task)

    # Stash the original so isinstance/reflection still work.
    wrapper.__wrapped__ = original  # type: ignore[attr-defined]
    return wrapper


class AsyncClient:
    """
    Wrap a synology-api instance and expose every public method as async.

    All public callable attributes of the wrapped instance are intercepted
    and re-dispatched via ``loop.run_in_executor``.  Non-callable attributes
    (properties, simple values) are returned as-is.

    Supports ``async with``::

        async with AsyncClient(fs) as client:
            await client.get_info()
        # fs.logout() is called on exit.

    Parameters
    ----------
    sync_instance : Any
        A fully-constructed synology-api instance (e.g.
        ``FileStation(...)``).  The wrapper does **not** accept a class
        — instantiate the class first, then wrap it.
    max_concurrency : int, optional
        Upper bound on simultaneous in-flight calls.  ``None`` (default)
        means unlimited.  Set a small value (e.g. 4) if your NAS drops
        sessions under heavy parallel load (observed on the DS218+).
    """

    __slots__ = ("_sync", "_cache", "_semaphore")

    def __init__(self, sync_instance: Any, max_concurrency: int | None = None) -> None:
        """
        Store the sync instance for later delegation.

        Parameters
        ----------
        sync_instance : Any
            A fully-constructed synology-api instance (e.g.
            ``FileStation(...)``).
        max_concurrency : int, optional
            Upper bound on simultaneous in-flight calls.  ``None`` means
            unlimited.
        """
        self._sync = sync_instance
        self._cache: dict[str, Any] = {}
        self._semaphore = (
            asyncio.Semaphore(max_concurrency) if max_concurrency else None
        )

    def __getattr__(self, name: str) -> Any:
        """
        Intercept attribute access and return an awaitable wrapper for callables.

        Wrapped callables are memoized on first access, so ``functools.wraps``
        is applied once per method and the returned object is stable across
        repeated lookups.

        Parameters
        ----------
        name : str
            The attribute name to look up on the wrapped instance.

        Returns
        -------
        Any
            An awaitable wrapper if the attribute is callable, otherwise
            the raw attribute value.

        Raises
        ------
        AttributeError
            If the attribute does not exist on the wrapped instance and
            its name starts with an underscore.
        """
        if name.startswith("_"):
            raise AttributeError(name)

        if name in self._cache:
            return self._cache[name]

        try:
            attr = getattr(self._sync, name)
        except AttributeError:
            raise AttributeError(
                f"{type(self._sync).__name__!r} object has no attribute {name!r}"
            ) from None

        wrapped = _make_async_callable(attr, name, self._semaphore)
        self._cache[name] = wrapped
        return wrapped

    # -- async context manager support --------------------------------

    async def __aenter__(self) -> "AsyncClient":
        """
        Enter the async context manager (no-op).

        Returns
        -------
        AsyncClient
            The same AsyncClient instance.
        """
        return self

    async def __aexit__(self, *args: Any) -> None:
        """
        Exit the async context manager — calls ``logout()`` if available.

        Parameters
        ----------
        *args : Any
            Exception type, value, and traceback (standard ``__aexit__``
            signature).
        """
        if hasattr(self._sync, "logout"):
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, self._sync.logout)
