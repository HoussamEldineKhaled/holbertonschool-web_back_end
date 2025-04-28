#!/usr/bin/env python3
"""measure runtime"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure the time

    Args:
       n: number of coroutines to execute
       max_delay: maximum delay for each coroutine

    Returns: Average execution time per coroutine
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total_time = end - start
    return total_time / n
