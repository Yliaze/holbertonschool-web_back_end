#!/usr/bin/env python3
"""Asynchronous coroutine that spawn wait_random n times
with task_wait_random being called"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay"""
    list_corouts = [task_wait_random(max_delay) for i in range(n)]
    unpack = await asyncio.gather(*list_corouts)
    return sorted(unpack)
