#!/usr/bin/env python3
"""
    Concurrent coroutines
"""
from typing import List
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Returns the list of all the delays
    """
    delays = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(delays)
