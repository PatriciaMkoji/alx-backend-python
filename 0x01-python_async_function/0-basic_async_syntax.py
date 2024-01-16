#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument (max_delay
"""


import random
import asyncio


async def wait_random(int: max_delay = 10) -> float:
    """ basic syntax of await """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
