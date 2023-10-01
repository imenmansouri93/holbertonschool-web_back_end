#!/usr/bin/env python3
"""
asynchronously wait 1 second, then yield a random number
between 0 and 10. Use the random module.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous  that yields a random number between 0 & 10 after waiting for 1 scd
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
