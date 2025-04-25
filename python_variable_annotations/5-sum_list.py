#!/usr/bin/env python3
"""list of floats"""


def sum_list(input_list: list[float]) -> float:
    """

    Args:
       input_list: list of floats

    Returns: sum of floats
    """
    count: float = 0
    for i in range(0, len(input_list)):
        count += input_list[i]
    return count
