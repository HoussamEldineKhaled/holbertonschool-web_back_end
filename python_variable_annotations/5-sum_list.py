#!/usr/bin/env python3
"""list of floats"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """

    Args:
       input_list: list of floats

    Returns: sum of floats
    """
    count: float = 0
    for i in range(0, len(input_list)):
        count += input_list[i]
    return count
