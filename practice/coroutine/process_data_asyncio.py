import asyncio
import time


async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    return range(1000000)


async def process_data() -> list[int]:
    """
    Process data by fetching and doubling each element.

    Returns
    -------
    list[int]
        A list of integers where each element is doubled.
    """
    print("processing data")
    data_task = asyncio.create_task(fetch_data())
    await asyncio.sleep(2)

    processed_data = [i * 2 for i in await data_task]
    return processed_data
 

async def main():
    start = time.perf_counter()
    print("starting main...")
    result = await process_data()
    print(f"Result : {result}")
    end = time.perf_counter()
    print(f"time = {end-start}")


asyncio.run(main())
