#!/usr/bin/env python3
"""asynchronous"""


import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    """

    Args:
       max_delay: maximum delayy

    Returns: the delay
    """
    delay = random.uniform(0, max_delay + 1)
    await asyncio.sleep(delay)
    return delay
