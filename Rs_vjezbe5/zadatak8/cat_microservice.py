from aiohttp import web, ClientSession
import asyncio

CATFACT_URL = "https://catfact.ninja/fact"

async def fetch_fact(session):
    async with session.get(CATFACT_URL) as resp:
        data = await resp.json()
        return data["fact"]

async def get_cats(request):
    amount = int(request.match_info["amount"])

    async with ClientSession() as session:
        tasks = [fetch_fact(session) for _ in range(amount)]
        facts = await asyncio.gather(*tasks)

    return web.json_response({"facts": facts})

app = web.Application()
app.router.add_get("/cat/{amount}", get_cats)

web.run_app(app, port=8086)
