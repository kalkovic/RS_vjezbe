import asyncio

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}

async def autentifikacija(username, password):
    await asyncio.sleep(2)  

    if username in korisnici and korisnici[username] == password:
        return True
    else:
        raise ValueError(f"Neispravni podaci za: {username}")


async def main():
    zahtjevi = [
        autentifikacija("korisnik1", "lozinka1"),   
        autentifikacija("korisnik2", "krivo"),      
        autentifikacija("korisnik3", "lozinka3"),   
        autentifikacija("fake", "fake"),            
        autentifikacija("korisnik2", "lozinka2"),   
    ]

    try:
        rezultati = await asyncio.gather(*zahtjevi)
        print(rezultati)
    except Exception as e:
        print("Dogodila se greška:", e)

asyncio.run(main())
