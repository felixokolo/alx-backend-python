#!/usr/bin/env python3
from typing import Iterable, List, Tuple, Sequence

"""
multiplier function
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    generates list of tuples

    Parameters:
        lst (Iterable): list to generate tuple
    Returns:
        list of tuples
    """
    return [(i, len(i)) for i in lst]
