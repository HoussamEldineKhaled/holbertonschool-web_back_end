#!/usr/bin/env python3
"""find the index range"""


import csv
import math
from typing import List


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
        """
        Get a page from the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns: list dataset
        """

        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        dataset = self.dataset()

        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []
        return dataset[start:end]
