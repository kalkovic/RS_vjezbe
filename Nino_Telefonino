pozivni_brojevi = {
    "01": ("Grad Zagreb i Zagrebačka županija", "Fiksna mreža"),
    "020": ("Dubrovačko-neretvanska županija", "Fiksna mreža"),
    "021": ("Splitsko-dalmatinska županija", "Fiksna mreža"),
    "022": ("Šibensko-kninska županija", "Fiksna mreža"),
    "023": ("Zadarska županija", "Fiksna mreža"),
    "031": ("Osječko-baranjska županija", "Fiksna mreža"),
    "032": ("Vukovarsko-srijemska županija", "Fiksna mreža"),
    "033": ("Virovitičko-podravska županija", "Fiksna mreža"),
    "034": ("Požeško-slavonska županija", "Fiksna mreža"),
    "035": ("Brodsko-posavska županija", "Fiksna mreža"),
    "040": ("Međimurska županija", "Fiksna mreža"),
    "042": ("Varaždinska županija", "Fiksna mreža"),
    "043": ("Bjelovarsko-bilogorska županija", "Fiksna mreža"),
    "044": ("Sisačko-moslavačka županija", "Fiksna mreža"),
    "047": ("Karlovačka županija", "Fiksna mreža"),
    "048": ("Koprivničko-križevačka županija", "Fiksna mreža"),
    "049": ("Krapinsko-zagorska županija", "Fiksna mreža"),
    "052": ("Istarska županija", "Fiksna mreža"),
    "053": ("Ličko-senjska županija", "Fiksna mreža"),
    "091": ("A1 Hrvatska", "Mobilna mreža"),
    "092": ("Tomato", "Mobilna mreža"),
    "095": ("Telemach", "Mobilna mreža"),
    "097": ("bonbon", "Mobilna mreža"),
    "098": ("Hrvatski Telekom", "Mobilna mreža"),
    "099": ("Hrvatski Telekom", "Mobilna mreža"),
    "060": ("Komercijalne usluge", "Posebne usluge"),
    "061": ("Usluge s dodanom vrijednošću", "Posebne usluge"),
    "064": ("Usluge za punoljetne korisnike", "Posebne usluge"),
    "065": ("Nagradne igre", "Posebne usluge"),
    "069": ("Usluge za djecu", "Posebne usluge"),
    "0800": ("Besplatan poziv", "Posebne usluge"),
    "072": ("Jedinstveni pristupni broj", "Posebne usluge")
}

def provjeri_broj(broj):
    broj = broj.strip()
    broj = broj.replace(" ", "")

    if broj.startswith("+385"):
        broj = "0" + broj[4:]

    if not broj.isdigit():
        return "Broj nije ispravno unesen. Dozvoljene su samo znamenke."

    for duljina in [4, 3, 2]:
        prefix = broj[:duljina]
        if prefix in pozivni_brojevi:
            info = pozivni_brojevi[prefix]
            return f"Pozivni broj: {prefix}\nPodručje / operator: {info[0]}\nVrsta: {info[1]}"

    return "Pozivni broj nije prepoznat."

print(provjeri_broj("0976543210"))
print(provjeri_broj("+38512345678a"))
print(provjeri_broj("0800123456"))
print(provjeri_broj("061123456"))