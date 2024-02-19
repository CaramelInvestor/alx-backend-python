#!/usr/bin/env python3
"""This file execute multiple coroutines at
the same time with async"""

import asyncio
from typing import List
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with
    the specified max_delay. Returns a list of all the delays
    (float values) in ascending order.
    """
    return sorted(await asyncio.gather(*(wait_random(max_delay) for _ in range(n))))
