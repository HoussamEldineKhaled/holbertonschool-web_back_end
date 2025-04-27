#!/usr/bin/env python3
"""complex string and int float to tuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """

    Args:
       k: string
       v float or integer

    Returns: a tuple
    """
    return (str, float(v ** 2))
