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
    """Wrap a sync callable so it runs in the default thread-pool executor.

    ``name`` is kept only for debug/traceback readability.
    """
    if not callable(original):
        return original

    @functools.wraps(original)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        loop = asyncio.get_running_loop()
        # functools.partial avoids closure-vs-loop issues.
        task = functools.partial(original, *args, **kwargs)
        return await loop.run_in_executor(None, task)

    # Stash the original so isinstance/reflection still work.
    wrapper.__wrapped__ = original  # type: ignore[attr-defined]
    return wrapper


class AsyncClient:
    """Wrap a synology-api *instance* and expose every public method as async.

    All public callable attributes of the wrapped instance are intercepted
    and re-dispatched via ``loop.run_in_executor``.  Non-callable attributes
    (properties, simple values) are returned as-is.

    Supports ``async with``::

        async with AsyncClient(fs) as client:
            await client.get_info()
        # fs.logout() is called on exit.
    """

    __slots__ = ("_sync",)

    def __init__(self, sync_instance: Any) -> None:
        # Accept either a ready-made instance or a class+args (constructor call).
        self._sync = sync_instance

    def __getattr__(self, name: str) -> Any:
        # Bypass the wrapper for __-prefixed attributes and non-callables.
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
        return self

    async def __aexit__(self, *args: Any) -> None:
        if hasattr(self._sync, "logout"):
            await _make_async_callable(self._sync.logout, "logout")()
