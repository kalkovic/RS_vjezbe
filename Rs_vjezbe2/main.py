from shop.proizvodi import *
from shop.narudzbe import *

for p in proizvodi_za_dodavanje:
    dodaj_proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])

print("Skladište:")
for s in skladiste:
    s.ispis()

naručeni = [
    {"naziv": "Laptop", "naručena_kolicina": 2},
    {"naziv": "Monitor", "naručena_kolicina": 1},
    {"naziv": "Tipkovnica", "naručena_kolicina": 3}
]

narudzba = napravi_narudzbu(naručeni)
narudzba.ispis_narudzbe()
