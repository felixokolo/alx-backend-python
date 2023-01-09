#!/usr/bin/env python3
"""
Basics of async
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits a random number of seconds

    Parameters:
        max_delay (int): maximum delay time in secs

    Returns:
        wait_time
    """
    random.seed(343)
    wait_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
