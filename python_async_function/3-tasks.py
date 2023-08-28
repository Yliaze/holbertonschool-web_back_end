#!/usr/bin/env python3
"""Function task_wait_random that returns a asyncio.Task"""
import asyncio
import random
import time
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an integer max_delay and returns a asyncio.Task"""
    obj = asyncio.create_task(wait_random(max_delay))
    return obj
