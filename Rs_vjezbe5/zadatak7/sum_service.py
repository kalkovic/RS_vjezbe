from aiohttp import web

async def zbroj(request):
    data = await request.json()
    brojevi = data.get("brojevi")

    if not brojevi:
        return web.json_response(
            {"error": "Nisu poslani brojevi"},
            status=400
        )

    return web.json_response({
        "zbroj": sum(brojevi)
    })

app = web.Application()
app.router.add_post("/zbroj", zbroj)

web.run_app(app, port=8083)
