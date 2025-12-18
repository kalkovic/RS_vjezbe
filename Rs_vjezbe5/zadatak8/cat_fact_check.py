from aiohttp import web

async def check_facts(request):
    data = await request.json()
    facts = data.get("facts", [])

    filtered = [
        f for f in facts
        if "cat" in f.lower() or "cats" in f.lower()
    ]

    return web.json_response({"filtered_facts": filtered})

app = web.Application()
app.router.add_post("/facts", check_facts)

web.run_app(app, port=8087)
