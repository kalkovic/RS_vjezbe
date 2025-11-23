import asyncio

async def autentifikacija():#fake auth koji pukne
    await asyncio.sleep(5)
    raise Exception

async def timer(sec : int):
    print(f"Izvršen timer {sec}")
    await asyncio.sleep(sec)
    print(f"Završavam čekanje timer {sec}")
    return f"Rezultat timera {sec}"

async def main():
    #timer_cor_1 =  timer(1)
    #timer_cor_2 =  timer(2)
    #timer_cor_3 =  timer(3)

    #task_1 = asyncio.create_task(timer_cor_1) #schedule
    #task_2 = asyncio.create_task(timer_cor_2) #schedule
    #task_3 = asyncio.create_task(timer_cor_3) #schedule

    lista_korutina = [timer(n) for n in range(1,6)]
    #lista_korutina = [asynchio.create_task(timer(n)) for n in range(1,6)] moze se i ovako ali je redundatno

    rezultat = await asyncio.gather(*lista_korutina, autentifikacija())

    #rezultat = await asyncio.gather(timer_cor_1, timer_cor_2, timer_cor_3) #schedule and run and gather results

    #rezultat = await task_2 #ovdje se event loop gasi
    print(rezultat)

asyncio.run(main())

"""
Pitanje na kolokviju kako se izvrsava event loop
"""