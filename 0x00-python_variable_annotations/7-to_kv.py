#!/usr/bin/env python3
"""
string iint/float to tuple
"""
from typing import List, Union, Tuple


def to_kv(k: str,
          v: Union[int,
                   float]) -> Tuple[str, float]:
    """
    To tuple

    Parameters:
        k (str): tuple string
        v (number): tuple float or int
    Returns:
        tuple (k, v)
    """
    return (k, v ** 2)
