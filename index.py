import asyncio
import time

"""async def korutina():
    print("nešto")
    print(asyncio.get_event_loop())
    await asyncio.sleep(3)
    print("opet nešto")
    return "Nešto treće"

asyncio.run(korutina())"""

"""def fecth_data(parametar):
    print(f"Delam nešto s {parametar}")
    time.sleep(3)
    return f"fetch_data rezultat: {parametar}"

def main():
    print("Izvršavam main funkciju")
    rezultat_1 = fecth_data(3)
    rezultat_2 = fecth_data(2)
    print("Završavam main funkciju...")
    return rezultat_1, rezultat_2

t1 = time.perf_counter()
main()
t2 = time.perf_counter()

print(f"Vrijeme izvršavanja je : {round(t2 - t1, 2)} sekundi")"""

"""""
async def fecth_data(parametar):
    print(f"Delam nešto s {parametar}")
    await asyncio.sleep(parametar)
    print(f"Završavamo fetch data funkciju...")
    return f"fetch_data rezultat: {parametar}"

async def main():
    print("Izvršavam main funkciju")
    task_1 = fecth_data(1)
    task_2 = fecth_data(2)
    rezultat_1 = await task_1
    rezultat_2 = await task_2
    print("Završavam main funkciju...")
    return rezultat_1, rezultat_2

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f"Vrijeme izvršavanja je : {round(t2 - t1, 2)} sekundi")"""

"""""
async def fecth_data(parametar):
    print(f"Delam nešto s {parametar}")
    await asyncio.sleep(parametar)
    print(f"Završavamo fetch data funkciju...")
    return f"fetch_data rezultat: {parametar}"

async def main():
    print("Izvršavam main funkciju")
    task_1 = asyncio.create_task(fecth_data(1))
    task_2 = asyncio.create_task(fecth_data(2))
    rezultat_1 = await task_1
    rezultat_2 = await task_2
    print("Završavam main funkciju...")
    return rezultat_1, rezultat_2

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f"Vrijeme izvršavanja je : {round(t2 - t1, 2)} sekundi")"""

async def fecth_data(parametar):
    print(f"Delam nešto s {parametar}")
    await asyncio.sleep(parametar)
    print(f"Završavamo fetch data funkciju...")
    return f"fetch_data rezultat: {parametar}"

async def main():
    print("Izvršavam main funkciju")
    task_1 = asyncio.create_task(fecth_data(2))
    task_2 = asyncio.create_task(fecth_data(3))
    rezultat_2 = await task_2
    rezultat_1 = await task_1
    print("Završavam main funkciju...")
    return rezultat_1, rezultat_2

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f"Vrijeme izvršavanja je : {round(t2 - t1, 2)} sekundi")