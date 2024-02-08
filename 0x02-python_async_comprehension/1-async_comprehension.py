#!/usr/bin/env python3
"""Async Comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect and return a list of 10 random numbers from async_generator.
    """
    return [i async for i in async_generator()]
