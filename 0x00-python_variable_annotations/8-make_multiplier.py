#!/usr/bin/env python3
"""
multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Generate multiplier function

    Parameters:
        multiplier (float): multiplier in function
    Returns:
        callable multiplier function
    """
    return lambda x: x * multiplier
