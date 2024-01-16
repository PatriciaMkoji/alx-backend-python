#!/usr/bin/env python3
"""
take the code from wait_n and alter it into a new function
task_wait_n. The code is nearly identical to wait_n except.
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ task """
    tasks = []
    delays = []

    for i in range(n):

        task = task_wait_random(max_delay)
        tasks.append(task)

        for task in asyncio.as_completed((tasks)):
            delay = await task
            delays.append(delay)
            return delays
