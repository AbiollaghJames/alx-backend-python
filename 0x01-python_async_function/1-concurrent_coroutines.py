#!/usr/bin/env python3
""" mmodule that executes multiple coroutines """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    tasks each running wait_random.
    Use of asyncio.gather to run all tasks and
    adding delays to list in ascending order
    """
    all_delays: List[float] = []

    tasks = [wait_random(max_delay) for _ in range(n)]
    res = await asyncio.gather(*tasks)

    for res in sorted(res):
        all_delays.append(res)

    return all_delays
