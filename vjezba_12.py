def obrni_rjecnik(originalni_rjecnik):
    novi_rjecnik = {}
    for kljuc, vrijednost in originalni_rjecnik.items():
        novi_rjecnik[vrijednost] = kljuc
    return novi_rjecnik

def kreiraj_rjecnik_od_korisnika():
    dinamicni_rjecnik = {}
    while True:
        kljuc = input("Unesite KLJUČ (ili 'gotovo' za kraj): ").strip()
        
        if kljuc.lower() == 'gotovo':
            break
        
        vrijednost = input(f"Unesite VRIJEDNOST za ključ '{kljuc}': ").strip()
        
        dinamicni_rjecnik[kljuc] = vrijednost
        
    return dinamicni_rjecnik

moj_rjecnik = kreiraj_rjecnik_od_korisnika()

if moj_rjecnik:
    obrnuti_rjecnik = obrni_rjecnik(moj_rjecnik)
    print(f"Originalni rječnik: {moj_rjecnik}")
    print(f"Obrnuti rječnik: {obrnuti_rjecnik}")
else:
    print("Nije unesen nijedan par.")