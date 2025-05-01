#!/usr/bin/env python3
"""find the index range"""


import csv
import math
from typing import List
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
            assert page > 0 and isinstance(page, int), "page must be a positive integer"
            assert page_size > 0 and isinstance(page_size, int), "page_size must be a positive integer"

            dataset = self.dataset()

            start, end = index_range(page, page_size)

            if start >= len(dataset):
                return []
            return dataset[start:end]
