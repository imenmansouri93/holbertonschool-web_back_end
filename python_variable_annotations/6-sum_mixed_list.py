#!/usr/bin/env python3
"""
Computes the sum of a list of integers and floats as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list
    """
    return float(sum(mxd_lst))
