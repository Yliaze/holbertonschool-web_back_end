#!/usr/bin/env python3
"""Coroutine called async_comprehension using
an async comprehensing over async_generator"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This coroutine will collect 10 random numbers using
    an async comprehensing over async_generator"""
    result = [i async for i in async_generator()]
    return result
