import asyncio
import aiohttp

async def fetch_url(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=5) as resp:
            return await resp.text()

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
    ]

    tasks = [fetch_url(url) for url in urls]

    results = await asyncio.gather(*tasks)

    for url, content in zip(urls, results):
        print(f"Fetched {len(content)} characters from {url}")

asyncio.run(main())
