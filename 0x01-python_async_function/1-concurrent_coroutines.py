#!/usr/bin/env python3
"""
This Module contains an async routine called wait_n that takes
in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""
import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    return the list of all the delays (float values)
    """
    delay_list = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return delay_list
