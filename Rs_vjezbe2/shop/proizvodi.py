skladiste = []

class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"{self.naziv} - {self.cijena} eur ({self.dostupna_kolicina} kom)")

def dodaj_proizvod(naziv, cijena, dostupna_kolicina):
    novi = Proizvod(naziv, cijena, dostupna_kolicina)
    skladiste.append(novi)

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100},
]