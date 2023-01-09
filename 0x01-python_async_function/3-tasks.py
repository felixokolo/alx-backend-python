#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Waits a random number of seconds

    Parameters:
        max_delay (int): maximum delay time in secs

    Returns:
        wait_time
    """

    return asyncio.create_task(wait_random(max_delay))
