from aiohttp import web

async def kolicnik(request):
    data = await request.json()
    zbroj = data.get("zbroj")
    umnozak = data.get("umnozak")

    if zbroj == 0:
        return web.json_response(
            {"error": "Dijeljenje s nulom"},
            status=400
        )

    return web.json_response({
        "kolicnik": umnozak / zbroj
    })

app = web.Application()
app.router.add_post("/kolicnik", kolicnik)

web.run_app(app, port=8085)
