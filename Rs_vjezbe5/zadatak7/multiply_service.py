from aiohttp import web
from functools import reduce
import operator

async def umnozak(request):
    data = await request.json()
    brojevi = data.get("brojevi")

    if not brojevi:
        return web.json_response(
            {"error": "Nisu poslani brojevi"},
            status=400
        )

    rezultat = reduce(operator.mul, brojevi, 1)
    return web.json_response({"umnozak": rezultat})

app = web.Application()
app.router.add_post("/umnozak", umnozak)

web.run_app(app, port=8084)
