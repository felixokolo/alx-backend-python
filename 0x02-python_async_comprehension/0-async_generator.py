#!/usr/bin/env python3
"""
Async Generator
"""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator function

    Returns:
        random number
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
