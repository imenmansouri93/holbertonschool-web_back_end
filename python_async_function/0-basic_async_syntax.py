#!/usr/bin/env python3
"""
module for the delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
