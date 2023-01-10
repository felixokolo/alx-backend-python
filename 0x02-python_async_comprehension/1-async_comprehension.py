#!/usr/bin/env python3
"""
Async Generator
"""

from typing import AsyncGenerator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """
    Asynchronous generator function

    Returns:
        random number
    """

    return [x async for x in async_generator()]
