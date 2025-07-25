#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """
        Args:
           index: the index of the page
           page_size: number of items in a page

        Returns: dictionairy
        """

        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        data = []
        current_index = index if index is not None else 0
        next_index = current_index
        count = 0

        while count < page_size and next_index < len(indexed_data):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
                count += 1
            next_index += 1

        return {'index': current_index, 'data': data,
                'page_size': len(data),
                'next_index': next_index if next_index <
                len(indexed_data) else None}
