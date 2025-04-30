#!/usr/bin/env python3
import asyncio
import random


async def async_generator():
    """asynchronous generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform() * 10
