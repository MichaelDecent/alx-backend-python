#!/usr/bin/env python3
"""
This Module contains an async routine called task_wait_n that takes
in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""
import asyncio
import typing

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Spawn wait_random n times and returns the list
    of all the delays (float values)
    """
    delay_list = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n)))
    for i in range(len(delay_list) - 1):
        swapped = False
        for j in range(0, len(delay_list) - i - 1):
            if delay_list[j] > delay_list[j + 1]:
                delay_list[j], delay_list[j + 1] = \
                    delay_list[j + 1], delay_list[j]
                swapped = True
        if not swapped:
            break

    return delay_list
