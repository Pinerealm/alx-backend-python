#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield random numbers between 0 and 10 every second for 10 seconds.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
