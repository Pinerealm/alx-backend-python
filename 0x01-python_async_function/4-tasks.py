#!/usr/bin/env python3
"""Execute multiple coroutines at the same time"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): number of times to execute task_wait_random
        max_delay (int): max wait time for task_wait_random

    Returns:
        list: list of all the delays (float values)
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
