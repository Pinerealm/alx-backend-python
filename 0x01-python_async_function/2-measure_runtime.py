#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for the wait_n function which
    executes the wait_random function n times with the specified max_delay.

    Args:
        n (int): number of times to execute wait_random
        max_delay (int): max wait time for wait_random

    Returns:
        float: total execution time
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
