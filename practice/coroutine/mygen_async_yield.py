import asyncio
import time

async def mygen(u: int = 10):
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.55)
    

async def f():
    [i async for i in mygen()]
    # return f_list

async def g():
    [j async for j in mygen() if not j // 3 % 5]
    # return g_list

async def main():
    
    f_task = asyncio.create_task(f())
    g_task = asyncio.create_task(g())

    start = time.perf_counter()
    await asyncio.gather(f_task, g_task)
    end = time.perf_counter()
    print(f"Total time {end - start}")
    # print(f)
    # print(g)


if __name__ == "__main__":
    asyncio.run(main())