#!/usr/bin/env python3
""" Module that uses async generator """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Generator function that yields random floats """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
