import requests
import aiohttp
import time
import asyncio

#lista = []
#t1 = time.perf_counter()# timestamp 1

"""for i in range(10):
    print(f"Šaljem request za fact {i}")
    response = requests.get("https://catfact.ninja/fact")
    lista.append(response.json()["fact"])
t2 = time.perf_counter()# timestamp 2
"""
#context manager se korist za I/O operacije
#with

#asinkroni context manager

async def dohvati_cat_fact(session : aiohttp.ClientSession):
        response = await session.get("https://catfact.ninja/fact")
        #deserijalizacija
        podatak = await response.json()["fact"]
        return podatak

async def main():
  async with aiohttp.ClientSession() as session:
      rezultati = await asyncio.gather[*(dohvati_cat_fact(session) for i in range(30))]
      print(rezultati)
      print("Završava main korutina")

    """rezultati = []
    for task in lista_taskova:
        rezultat_taska = await task
        rezultati.append(rezultat_taska)
        print(rezultati)
    """

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

#aiohttp.ClientSession()

#print(lista)
print(f"Vrijeme izvršavanja {round(t2 - t1:.2f)}")