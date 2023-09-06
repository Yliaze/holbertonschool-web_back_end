#!/usr/bin/env python3
"""Function index_range, class Server"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of size two, indicating the start and end
    indexes that define the range of indexes to retrieve from a
    list based on the given pagination parameters."""
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary containing key-value pairs"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        """The dataset page"""
        dataset_page = self.get_page(page, page_size)

        """Number of the next page"""
        if end_index >= len(dataset):
            next_page = None
        else:
            next_page = page + 1

        """Number of the previous page"""
        if page - 1 < 1:
            prev_page = None
        else:
            prev_page = page - 1

        """Total number of pages in the dataset"""
        total_pages = math.ceil(len(dataset) / page_size)

        """Dictionary construction"""
        hyper_dict = {
            "page_size": page_size,
            "page": page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }

        return hyper_dict
