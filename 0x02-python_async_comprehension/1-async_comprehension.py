#!/usr/bin/env python3
""" Module that collects 10 random numbers
    and display then in a list using async
    comprehension
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine that uses async comprehension to
    return list of random floats
    """
    res = [i async for i in async_generator()]
    return res
