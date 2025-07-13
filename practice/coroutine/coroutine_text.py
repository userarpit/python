import asyncio

async def fetch_data(data_id: int) -> str:
    print(f"Fetching data {data_id}...")
    await asyncio.sleep(3)  # Simulate a network delay
    print(f"Data {data_id} fetched.")
    return f"Data {data_id}"

# async def compute_result(value: int) -> int:
#     print(f"Computing result for {value}...")
#     await asyncio.sleep(5)  # Simulate a computation delay
#     print(f"Result for {value} computed.")
#     return value * 2

# async def process_data() -> None:
#     data = await fetch_data(1)
#     result = await compute_result(5)
#     print(f'Result: {result}')
#     print(f"Data: {data}")

# async def process_data() -> None:
#     start_time = asyncio.get_event_loop().time()
#     print(f"Start time: {start_time}")

#     await fetch_data(1)
#     await fetch_data(2)
#     await fetch_data(3)

#     end_time = asyncio.get_event_loop().time()
#     print(f"End time: {end_time}")

#     print(f"Total time taken is {float(end_time - start_time):.2f} seconds")

# with task
async def process_data() -> None:
    start_time = asyncio.get_event_loop().time()
    print(f"Start time: {start_time}")

    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2)) 
    task3 = asyncio.create_task(fetch_data(3))

    # await task1
    # await task2
    # await task3

    await asyncio.gather(task1, task2, task3)
    end_time = asyncio.get_event_loop().time()
    print(f"End time: {end_time}")

    print(f"Total time taken is {float(end_time - start_time):.2f} seconds")

asyncio.run(process_data())
