#!/usr/bin/env python3
"""
Async Generator
"""

import time
import asyncio
from typing import AsyncGenerator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous generator function

    Returns:
        random number
    """

    start = time.perf_counter()
    await asyncio.gather(*([async_comprehension()] * 4))
    stop = time.perf_counter()
    return stop - start
