#!/usr/bin/env python3
"""
Pagination working with the server class, returning dictionaries
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    returns start and end index and size
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a page of the dataset
        """
        assert isinstance(page, int) and page > 0, "Page must "
        "be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size "
        "must be a positive integer"

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        returns a dictionary of the hypermedia information
        """
        assert isinstance(page, int) and page > 0, "Page must "
        "be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size "
        "must be a positive integer"

        dataset = self.get_page(page, page_size)
        total = math.ceil(len(self.dataset()) / page_size)
        next = page + 1 if page < total else None
        prev = page - 1 if page > 1 else None

        return {
            'page_size': len(dataset),
            'page': page,
            'data': dataset,
            'next_page': next,
            'prev_page': prev,
            'total_pages': total
        }
