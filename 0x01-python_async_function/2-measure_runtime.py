#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Waits a random number of seconds

    Parameters:
        max_delay (int): maximum delay time in secs

    Returns:
        wait_time
    """

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop = time.perf_counter()
    ret = (stop - start) / n

    return ret
