#!/usr/bin/env python3
"""
    This script measures the runtime of a function.
"""
wait_n = __import__("1-concurrent_coroutines").wait_n
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
        measure the time of the function
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
