#!/usr/bin/env python3
from typing import Iterable, List, Tuple

"""
multiplier function
"""


def element_length(lst: Iterable) -> List[Tuple[Iterable, int]]:
    """
    generates list of tuples

    Parameters:
        lst (Iterable): list to generate tuple
    Returns:
        list of tuples
    """
    return [(i, len(i)) for i in lst]
