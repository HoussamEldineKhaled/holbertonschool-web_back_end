#!/usr/bin/env python3
"""multiplier annotation"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """annotation

    Args:
       multiplier: the multiplier

    Returns: multiplier
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
