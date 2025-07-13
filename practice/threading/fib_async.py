import asyncio

import time


async def fib(number: int) -> int:
    return number if number < 2 else await fib(number - 2) + await fib(number - 1)


async def main():
    start = time.perf_counter()
    tasks = [fib(35) for _ in range(20)]

    results = await asyncio.gather(*tasks)
    print(f"total time = {time.perf_counter() - start} seconds")

    print(results)


if __name__ == "__main__":
    asyncio.run(main())
