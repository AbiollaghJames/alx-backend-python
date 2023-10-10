#!/usr/bin/env python3
""" module identical to wait_n """

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return tasks in ascending """
    all_delays: List[float] = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    res = await asyncio.gather(*tasks)

    for res in sorted(res):
        all_delays.append(res)

    return all_delays
