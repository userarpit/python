import asyncio
import random

async def my_task(lock, a: int):
    n = random.randint(1,10)
    print(f"resource {a} for {n} seconds")
    await asyncio.sleep(n,)
    
    async with lock:
        print(f"lock acquired on {a}")

async def main() -> None:
    lock = asyncio.Lock()
    await asyncio.gather(my_task(lock, 1), my_task(lock, 2), my_task(lock, 23))


if __name__ == "__main__":
    random.seed(444)
    asyncio.run(main())