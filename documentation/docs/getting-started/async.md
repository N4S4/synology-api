# Async Client

`synology-api` includes an async wrapper that makes any synchronous API class awaitable — without duplicating a single line of business logic.

```bash
pip install synology-api
```

No extra dependencies needed — the wrapper uses only `asyncio` from the standard library.

## Quick Start

```python
import asyncio
from synology_api.filestation import FileStation
from synology_api.photos import Photos
from synology_api.async_client import AsyncClient

async def main():
    # Wrap any existing synology-api class
    fs = AsyncClient(FileStation(
        "192.168.1.x", "5001", "admin", "password",
        secure=True, cert_verify=False, dsm_version=7,
    ))
    ph = AsyncClient(Photos(
        "192.168.1.x", "5001", "admin", "password",
        secure=True, cert_verify=False, dsm_version=7,
    ))

    # Every method is automatically awaitable
    info = await fs.get_info()
    files = await fs.get_file_list("/home")

    user = await ph.get_userinfo()
    folders = await ph.list_folders(0, 0, 5)

asyncio.run(main())
```

## Concurrent Calls

The real advantage of async is running multiple operations in parallel:

```python
import asyncio
from synology_api.filestation import FileStation
from synology_api.async_client import AsyncClient

async def main():
    fs = AsyncClient(FileStation(...))

    # Three folder listings run concurrently
    home, photo, music = await asyncio.gather(
        fs.get_file_list("/home"),
        fs.get_file_list("/photo"),
        fs.get_file_list("/music"),
    )
    # ~3x faster than calling them sequentially

asyncio.run(main())
```

## How It Works

`AsyncClient` intercepts every public method call on the wrapped instance and dispatches it to a thread-pool executor via `loop.run_in_executor()`. The underlying synchronous HTTP calls run in worker threads, freeing the event loop for other tasks.

## Cleanup

Use `async with` to ensure the session is logged out:

```python
async with AsyncClient(FileStation(...)) as fs:
    info = await fs.get_info()
# fs.logout() is called automatically on exit
```
