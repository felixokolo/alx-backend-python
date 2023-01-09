#!/usr/bin/env python3
"""
Let's execute multiple coroutines
at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits a random number of seconds

    Parameters:
        max_delay (int): maximum delay time in secs

    Returns:
        wait_time[asyncio
                                  .create_task(wait_random(max_delay))] * n
    """

    task_wait_random = asyncio.create_task(wait_random(max_delay))
    ret = await asyncio.gather(*([task_wait_random]) * n
                               )

    return sorted(ret)
