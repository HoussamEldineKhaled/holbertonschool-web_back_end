#!/usr/bin/env python3
"""many coroutines"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random



async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait n times and record delay times"""
    list_time = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for i in asyncio.as_completed(tasks):
        delay = await i
        list_time.append(delay)

    return list_time
