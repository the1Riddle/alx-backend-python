#!/usr/bin/env python3
"""
    a function that takes a int max_delay and returns a asyncio.Task
    using a regular function syntax
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        returns a asyncio.Task
    """
    return (asyncio.create_task(wait_random(max_delay)))
