import asyncio
import aiohttp

async def call_service(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as resp:
            return await resp.json()

async def main():
    data = {"brojevi": [2, 4, 6]}

    zbroj_task = call_service("http://localhost:8083/zbroj", data)
    umnozak_task = call_service("http://localhost:8084/umnozak", data)

    zbroj_res, umnozak_res = await asyncio.gather(zbroj_task, umnozak_task)

    payload = {
        "zbroj": zbroj_res["zbroj"],
        "umnozak": umnozak_res["umnozak"]
    }

    kolicnik = await call_service("http://localhost:8085/kolicnik", payload)
    print(kolicnik)

asyncio.run(main())
