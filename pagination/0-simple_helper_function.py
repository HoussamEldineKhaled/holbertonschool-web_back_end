#!/usr/bin/env python3
"""find the index range"""


from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """Calculate the start and end index

    Args:
       page: page number
       page_size: number items per page

    Returns: (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
