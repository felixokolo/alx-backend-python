#!/usr/bin/env python3
"""
Sum of a list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums all elements in a li  st

    Parameters:
        mxd_lst (list): list to sum all elements
    Returns:
        sum of all elements
    """
    return sum(mxd_lst)
