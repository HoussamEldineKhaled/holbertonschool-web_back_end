#!/usr/bin/env python3
"""summation of a mixed list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum a mixed list

    Args:
       mxd_lst: mixed list of floats and ints

    Returns: summations
    """
    return sum(mxd_lst)
