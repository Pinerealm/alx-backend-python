#!/usr/bin/env python3
"""The basics of async"""
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously returns a float value between 0 and max_delay

    Args:
        max_delay (int, optional): The maximum value of the delay.

    Returns:
        float: The generated random float value.
    """
    import random
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
