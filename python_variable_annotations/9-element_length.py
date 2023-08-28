#!/usr/bin/env python3
"""Type-annotated function element_length"""
from typing import Tuple, Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes a Sequence as argument and returns a
    list of tuple of Sequence and int"""
    return [(i, len(i)) for i in lst]
