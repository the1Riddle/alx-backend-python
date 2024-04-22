#!/usr/bin/env python3

"""
    an asynchronous coroutine that takes in
    an integer argument (max_delay, with a
    default value of 10) named wait_random that waits
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        takes a random seconds
    """
    delay: float  = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
