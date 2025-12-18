import asyncio
import aiohttp
import time

async def send_request(url, port):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://{url}:{port}/pozdrav") as resp:
            return await resp.json()

async def main():
    start = time.perf_counter()

    r1 = await send_request("localhost", 8081)
    r2 = await send_request("localhost", 8082)

    end = time.perf_counter()

    print("Sekvencijalno:")
    print(r1)
    print(r2)
    print(f"Vrijeme: {end - start:.2f} s\n")

    start = time.perf_counter()

    results = await asyncio.gather(
        send_request("localhost", 8081),
        send_request("localhost", 8082)
    )

    end = time.perf_counter()

    print("Konkurentno:")
    for r in results:
        print(r)
    print(f"Vrijeme: {end - start:.2f} s")

asyncio.run(main())
