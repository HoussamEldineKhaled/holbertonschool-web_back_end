#!/usr/bin/env python3
"""tasks"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates and returns async tasks

    Args:
       max_delay: maximum delay

    Returns: async tasks
    """
    return asyncio.create_task(wait_random(max_delay))
