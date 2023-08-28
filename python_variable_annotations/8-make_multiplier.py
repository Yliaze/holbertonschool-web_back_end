#!/usr/bin/env python3
"""Type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float as argument and returns a
    function that multiplies a float by it"""
    def multiply(x: float) -> float:
        """Multiplies a float by the float argument"""
        return x * multiplier
    return multiply
