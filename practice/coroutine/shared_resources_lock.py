import random
import asyncio


async def access_shared_resource(lock, resource, task):
    n = random.randint(1, 10)
    print(f"task {task} sleep for {n} seconds")
    await asyncio.sleep(n)

    async with lock:
        # await asyncio.sleep(1)
        resource.append(random.randint(1, 100))
        print(f"{task} task updated the resource state to {resource}")


async def main() -> None:
    lock = asyncio.Lock()
    shared_resource = []
    tasks = [access_shared_resource(lock, shared_resource, task) for task in range(5)]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
