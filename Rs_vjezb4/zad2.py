import asyncio
import aiohttp

async def get_cat_fact(session):
    async with session.get("https://catfact.ninja/fact") as resp:
        data = await resp.json()
        return data["fact"]

async def filter_cat_facts(facts):
    out = []
    for f in facts:
        if "cat" in f.lower() or "cats" in f.lower():
            out.append(f)
    return out

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(20)]
        all_facts = await asyncio.gather(*tasks)

        filtered = await filter_cat_facts(all_facts)

        print("Filtrirane činjenice o mačkama:")
        for f in filtered:
            print("- " + f)

asyncio.run(main())