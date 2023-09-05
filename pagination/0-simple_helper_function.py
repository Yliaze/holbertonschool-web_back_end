#!/usr/bin/env python3
"""Function named index_range that takes two integer
arguments page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of size two, indicating the start and end
    indexes that define the range of indexes to retrieve from a
    list based on the given pagination parameters."""
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
