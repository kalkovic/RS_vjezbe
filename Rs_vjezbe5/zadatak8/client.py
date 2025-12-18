import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8086/cat/10") as r1:
            cats = await r1.json()

        async with session.post(
            "http://localhost:8087/facts",
            json=cats
        ) as r2:
            result = await r2.json()

        print(result)

asyncio.run(main())
