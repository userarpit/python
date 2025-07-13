import asyncio
import random
# import time


async def long_running_task():
    print("started long running task")
    duration = random.randint(1, 6)
    print(duration)
    await asyncio.sleep(duration)

    print("finished long running task")
    return duration


async def wait_with_timeout():
    # try:

    # start=time.perf_counter()
    # wait for long-running task to be complete in 5 seconds
    # await asyncio.wait_for(long_running_task(), timeout=5)
    # end=time.perf_counter()
    # print(f"Task is completed within {end-start:.2f} seconds")
    # except asyncio.TimeoutError:
    #     # handle timeout
    #     print("Task is timedout and could not be completed")

    # create task
    tasks = [asyncio.create_task(long_running_task()) for _ in range(5)]

    # wait for tasks to be completed within 10 second window
    done, pending = await asyncio.wait(tasks, timeout=3)

    for task in done:
        print(f"Task completed with result: {task.result()} seconds")

    for task in pending:
        print(f"Task timeout and cancelled.")
        task.cancel()


async def main() -> None:
    await wait_with_timeout()

async def test():
    print("test")

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.run_until_complete(test())
    loop.close()
    # asyncio.run(main())

    # # runner context
    # with asyncio.Runner() as runner:
    #     runner.run(main())
    #     runner.run(test())
