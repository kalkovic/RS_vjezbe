import aiohttp
import asyncio
import time

async def dohvati_korisnike(session):
    async with session.get("https://jsonplaceholder.typicode.com/users") as resp:
        return await resp.json()

async def main():
    async with aiohttp.ClientSession() as session:
        zadaci = [dohvati_korisnike(session) for _ in range(5)]
        rezultati = await asyncio.gather(*zadaci)

        imena = []
        emailovi = []
        usernames = []

        for lista in rezultati:
            for korisnik in lista:
                imena.append(korisnik["name"])
                emailovi.append(korisnik["email"])
                usernames.append(korisnik["username"])

        print("Imena:", imena)
        print("Emailovi:", emailovi)
        print("Usernames:", usernames)

        print("Main korutina završila.")

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f"Izvršavanje programa traje {t2 - t1:.2f} sekundi.")
