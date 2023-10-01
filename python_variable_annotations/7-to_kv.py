#!/usr/bin/env python3
"""
Returns a tuple with the string k and the square of int/float v as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
   to_kv function
    """
    result = float(v) ** 2  
    return k, result
