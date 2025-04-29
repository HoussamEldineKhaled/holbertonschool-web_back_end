#!/usr/bin/env python3
import asyncio
import random


def async_generator():
    """
    Async generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
