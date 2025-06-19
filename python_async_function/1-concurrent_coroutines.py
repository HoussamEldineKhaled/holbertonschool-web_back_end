#!/usr/bin/env python3
"""many coroutines"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait n times and record delay times

    Args:
      n: number of waits
      max_delay: maximum delay

    Returns: delays
    """
    delays = []
    if max_delay == 0:
        tasks = [wait_random(0) for _ in range(n)]
    else:
        tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
