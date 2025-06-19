#!/usr/bin/env python3
"""many coroutines"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: float) -> List[float]:
    """wait n times and record delay times

    Args:
      n: number of waits
      max_delay: maximum delay

    Returns: delays
    """
    
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
