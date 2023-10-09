#!/usr/bin/env python3
""" Async corountine using random module """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ coroutine that returns max_delay """
    rand_delay = random.uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay
