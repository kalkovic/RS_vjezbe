from aiohttp import web
import hashlib
import json

korisnici = [
    {"korisnicko_ime": "admin", "lozinka_hash": "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"},
    {"korisnicko_ime": "markoMaric", "lozinka_hash": "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"},
    {"korisnicko_ime": "ivanHorvat", "lozinka_hash": "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"},
    {"korisnicko_ime": "Nada000", "lozinka_hash": "492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"}
]

def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


async def register(request):
    data = await request.json()
    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")

    if not korisnicko_ime or not lozinka:
        return web.json_response({"poruka": "Nedostaju podaci"}, status=400)

    for k in korisnici:
        if k["korisnicko_ime"] == korisnicko_ime:
            return web.json_response({"poruka": "Korisnik već postoji"}, status=409)

    korisnici.append({
        "korisnicko_ime": korisnicko_ime,
        "lozinka_hash": hash_data(lozinka)
    })

    return web.json_response({"poruka": "Korisnik uspješno registriran"}, status=201)


async def login(request):
    data = await request.json()
    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")

    for k in korisnici:
        if k["korisnicko_ime"] == korisnicko_ime:
            if k["lozinka_hash"] == hash_data(lozinka):
                return web.json_response({"poruka": "Uspješna prijava"})
            else:
                return web.json_response({"poruka": "Pogrešna lozinka"}, status=401)

    return web.json_response({"poruka": "Korisnik ne postoji"}, status=404)


app = web.Application()
app.router.add_post("/register", register)
app.router.add_post("/login", login)

web.run_app(app, port=9000)
