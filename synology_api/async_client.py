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


def _make_async_callable(original: Any, name: str) -> Any:
    """
    Wrap a synchronous callable so it runs in the default thread-pool executor.

    ``name`` is kept only for debug/traceback readability.

    Parameters
    ----------
    original : Any
        The synchronous callable to wrap.
    name : str
        The attribute name, used only for debug/traceback context.

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
        Execute the wrapped callable in the default thread-pool executor.

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
        # functools.partial avoids closure-vs-loop issues.
        task = functools.partial(original, *args, **kwargs)
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
    """

    __slots__ = ("_sync",)

    def __init__(self, sync_instance: Any) -> None:
        """
        Store the sync instance for later delegation.

        Parameters
        ----------
        sync_instance : Any
            A fully-constructed synology-api instance (e.g.
            ``FileStation(...)``).
        """
        self._sync = sync_instance

    def __getattr__(self, name: str) -> Any:
        """
        Intercept attribute access and return an awaitable wrapper for callables.

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

        try:
            attr = getattr(self._sync, name)
        except AttributeError:
            raise AttributeError(
                f"{type(self._sync).__name__!r} object has no attribute {name!r}"
            ) from None

        return _make_async_callable(attr, name)

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
            await _make_async_callable(self._sync.logout, "logout")()
