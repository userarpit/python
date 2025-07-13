# SlingAcademy.com
# This code uses Python 3.11.4
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(1)
    print("Three")

async def hello() -> None:
    await asyncio.sleep(5)
    print("hello")


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(hello())
loop.close()