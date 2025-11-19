import asyncio
import time

async def fetch_data(param):
    print(f"Radim nešto {param}...")
    await asyncio.sleep(param)
    print(f"Dovršio sam s {param}.")
    return f"Rezultat {param}"

async def main():
    t1 = asyncio.create_task(fetch_data(1))
    t2 = asyncio.create_task(fetch_data(2))

    r1 = await t1

    print("Prvi task gotov.")
    return r1

start = time.perf_counter()
rezultat = asyncio.run(main())
end = time.perf_counter()

print("Rezultat maina:", rezultat)
print("Vrijeme:", round(end - start, 2), "s")
