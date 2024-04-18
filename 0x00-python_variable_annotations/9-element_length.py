#!/usr/bin/env python3
"""
    returns values with the appropriate type
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        returns values with the appropriate type
    """
    return [(i, len(i)) for i in lst]
