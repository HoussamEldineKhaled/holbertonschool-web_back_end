#!/usr/bin/env python3
"""duck type"""


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """

    Args:
       lst: an interable

    Returns: the element length
    """
    return [(i, len(i)) for i in lst]
