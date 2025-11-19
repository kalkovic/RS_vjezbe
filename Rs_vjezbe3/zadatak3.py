import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirkol23', 'email': 'mirkol23@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirkol23', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFFdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autorizacija(korisnik_iz_baze, lozinka):
    await asyncio.sleep(2)

    korisnicko_ime = korisnik_iz_baze['korisnicko_ime']

    lozinka_baza = ""
    for zapis in baza_lozinka:
        if zapis['korisnicko_ime'] == korisnicko_ime:
            lozinka_baza = zapis['lozinka']
            break

    if lozinka == lozinka_baza:
        return f"Korisnik {korisnicko_ime}: Autorizacija uspješna."
    else:
        return f"Korisnik {korisnicko_ime}: Autorizacija neuspješna."


async def autentifikacija(korisnik):
    await asyncio.sleep(3)

    korisnicko_ime = korisnik['korisnicko_ime']
    email = korisnik['email']
    lozinka = korisnik['lozinka']

    korisnik_iz_baze = None
    for zapis in baza_korisnika:
        if zapis['korisnicko_ime'] == korisnicko_ime and zapis['email'] == email:
            korisnik_iz_baze = zapis
            break

    if korisnik_iz_baze is None:
        return f"Korisnik {korisnicko_ime} nije pronađen."

    return await autorizacija(korisnik_iz_baze, lozinka)


async def main():
    korisnik = {
        "korisnicko_ime": "ana_anic",
        "email": "aanic@gmail.com",
        "lozinka": "super_teska_lozinka"
    }

    rezultat = await autentifikacija(korisnik)
    print(rezultat)


asyncio.run(main())
