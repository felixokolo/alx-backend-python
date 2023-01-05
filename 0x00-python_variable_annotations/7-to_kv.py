#!/usr/bin/env python3
from typing import List, Union, Tuple

"""
string iint/float to tuple
"""


def to_kv(k: str,
          v: List[Union[int,
                        float]]) -> Tuple[Union[str,
                                                Union[int,
                                                      float]]]:
    """
    To tuple

    Parameters:
        k (str): tuple string
        v (number): tuple float or int
    Returns:
        tuple (k, v)
    """
    return (k, v)
