#!/usr/bin/env python3
from typing import List

"""
Sum of a list
"""

def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    """
    Sums all elements in a li  st

    Parameters:
        mxd_lst (list): list to sum all elements
    Returns:
        sum of all elements
    """
    return sum(mxd_lst)
