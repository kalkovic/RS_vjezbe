from shop.proizvodi import skladiste

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        tekst = "Naručeni proizvodi: "
        lista = []
        for p in self.naruceni_proizvodi:
            lista.append(f"{p['naziv']} x {p['naručena_kolicina']}")
        tekst += ", ".join(lista)
        tekst += f", Ukupna cijena: {self.ukupna_cijena} eur"
        print(tekst)

def napravi_narudzbu(lista_narudzbi):
    naruceni = []
    ukupno = 0

    for nar in lista_narudzbi:
        naziv = nar["naziv"]
        kolicina = nar["naručena_kolicina"]

        proizvod = next((p for p in skladiste if p.naziv == naziv), None)
        if not proizvod:
            print(f"Proizvod {naziv} nije dostupan!")
            continue

        if proizvod.dostupna_kolicina < kolicina:
            print(f"Nema dovoljno proizvoda: {naziv}")
            continue

        proizvod.dostupna_kolicina -= kolicina
        naruceni.append({"naziv": naziv, "naručena_kolicina": kolicina})
        ukupno += proizvod.cijena * kolicina

    return Narudzba(naruceni, ukupno)
