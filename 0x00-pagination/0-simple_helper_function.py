#!/usr/bin/env python3
"""
return a tuple of size two containing a start index and an end index
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    returns start and end index and size
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
