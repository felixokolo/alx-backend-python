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
        wait_time
    """

    ret = await asyncio.gather(*([asyncio
                                  .create_task(wait_random(max_delay))] * n)
                               )

    return sorted(ret)


n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
