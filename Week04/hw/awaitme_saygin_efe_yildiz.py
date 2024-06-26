from typing import Callable, Awaitable
import asyncio

def awaitme(fn: Callable) -> Awaitable:
    async def _fn(*args, **kwargs):
        return fn(*args, **kwargs)
    return _fn