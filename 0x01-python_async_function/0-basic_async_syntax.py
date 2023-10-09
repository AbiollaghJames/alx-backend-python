#!/usr/bin/env python3
""" Async corountine using random module """

import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """ coroutine that returns max_delay """

    if isinstance(max_delay, (int, float)):
        rand_delay = random.uniform(0, max_delay)
        await asyncio.sleep(1)
        return rand_delay
