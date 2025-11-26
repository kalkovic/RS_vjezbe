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

"""
Evo jednostavnije i više “studentski” napisano
Event loop će normalno pokrenuti fetch_data(2) iako je ne čekamo u main funkciji, 
jer se task ubacuje u raspored čim pozovemo asyncio.create_task. Kad je task jednom kreiran, 
event loop ga sam izvršava u pozadini, bez obzira čeka li ga main ili ne.
Zato se ispis “Dovršio sam s 2.” svejedno pojavi. main čeka samo task1, 
ali event loop paralelno gura naprijed i task2, pa on završi i ispiše svoje poruke iako ga nismo eksplicitno awaitali. 
"""