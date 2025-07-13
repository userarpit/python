import asyncio
import sys
import time
import random


async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    return result


async def part2(n: int, p1:str) -> str:
    i = random.randint(0, 10)
    print(f"part2({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {p1}"
    return result


async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter()
    print(f"--> Chained Result({n}) => {p2} (took {(end-start):.2f} seconds).")


async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
    # random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()

    asyncio.run(main(*args))
    end = time.perf_counter()
    print(f"Total time taken is {float(end - start):.2f} seconds")