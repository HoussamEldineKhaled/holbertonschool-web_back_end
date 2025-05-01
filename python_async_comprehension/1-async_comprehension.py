#!/usr/bin/env python3
"""asynchronous comprehension"""


async_generator = __import__('0-async_generator').async_generator
from typing import List

async def async_comprehension() -> List[float]:
    """async comprehensions"""
    return [i async for i in async_generator()]
