#!/usr/bin/env python3
"""
    a functions that takes a string k and an int OR float v as arguments
    and returns a tuple, where the first element of the tuple
    is the string k.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        returns a tuple
    """
    return (k, v * v)
