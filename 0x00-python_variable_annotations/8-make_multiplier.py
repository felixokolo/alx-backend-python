#!/usr/bin/env python3
from typing import Callable

"""
multiplier function
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Generate multiplier function

    Parameters:
        multiplier (float): multiplier in function
    Returns:
        callable multiplier function
    """
    return lambda x: x * multiplier
