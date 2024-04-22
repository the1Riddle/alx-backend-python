#!/usr/bin/env python3
"""
    altering wait_n into a new function task_wait_n
    that can be called with the proper arguments.
"""
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        task_wait_random n times
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
