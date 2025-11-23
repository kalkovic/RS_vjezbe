import asyncio
import aiohttp

async def get_dog_fact(session):
    async with session.get("https://dogapi.dog/api/v2/facts") as resp_dog:
        data = await resp_dog.json()
        return data["data"][0]["attributes"]["body"]

async def get_cat_fact(session):
    async with session.get("https://catfact.ninja/fact") as resp_cat:
        data = await resp_cat.json()
        return data["fact"]

async def mix_facts(dog_facts, cat_facts):
    mixed = []
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            mixed.append(dog_fact)
        else:
            mixed.append(cat_fact)
    return mixed

async def main():
    async with aiohttp.ClientSession() as session:

        dog_tasks = [asyncio.create_task(get_dog_fact(session)) for _ in range(5)]

        cat_tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(5)]

        results = await asyncio.gather(*dog_tasks, *cat_tasks)

        dog_facts = results[:5]
        cat_facts = results[5:]

        final_list = await mix_facts(dog_facts, cat_facts)

        print("Miješane činjenice o psima i mačkama:\n")
        for fact in final_list:
            print("-", fact)

asyncio.run(main())