#!/usr/bin/env python3
"""Asynchronous coroutine that spawn wait_random n times
with the specified max_delay"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay"""
    list_corouts = [wait_random(max_delay) for i in range(n)]
    unpack = await asyncio.gather(*list_corouts)
    return sorted(unpack)
