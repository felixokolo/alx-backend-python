#!/usr/bin/env python3
"""
Async Generator
"""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """
    Asynchronous generator function

    Returns:
        random number
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
