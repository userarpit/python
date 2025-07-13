import asyncio
import aiohttp


async def fetch_data(url) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    result = await fetch_data("https://api.slingacademy.com/")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
