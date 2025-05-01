#!/usr/bin/env python3
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """asynchronous generator"""
    for _ in range(10):
        yield random.uniform(0, 10)
