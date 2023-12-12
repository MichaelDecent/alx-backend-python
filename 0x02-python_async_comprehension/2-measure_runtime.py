#!/usr/bin/env python3
"""
This Module cotains a function measure_runtime should
measure the total runtime and return it
"""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    measures the total runtime and return it.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elapsed = time.perf_counter()

    return elapsed - start
