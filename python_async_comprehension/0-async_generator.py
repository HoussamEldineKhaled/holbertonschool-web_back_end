#!/usr/bin/env python3
import asyncio
import random
import time


async def async_generator():
    """asynchronous generator"""
    async for _ in range(10):
        await asyncio.wait(1)
        yield random.uniform(0, 10)
