#!/usr/bin/env python3
"""
Returns a function that multiplies a float by the given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier function
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
