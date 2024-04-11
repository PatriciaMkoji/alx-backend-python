#!/usr/bin/env python3
"""
Asynchronous co-routine that takes in an integer argument
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for some time"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time