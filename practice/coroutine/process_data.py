import asyncio
import time

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    return range(1000000)

async def process_data():
    print("processing data")
    data = await fetch_data()
    await asyncio.sleep(2)

    return [i*2 for i in data]

async def main():
    start = time.perf_counter()
    print("starting main...")
    result = await process_data()
    # print(f"Result : {result}")
    end=time.perf_counter()
    print(f"time = {end-start}")

asyncio.run(main())