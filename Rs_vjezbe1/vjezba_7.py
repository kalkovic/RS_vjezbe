def provjera_lozinke(lozinka):
  
    duljina = len(lozinka)
    if not (8 <= duljina <= 15):
        print("Lozinka mora sadržavati između 8 i 15 znakova.")
        return False

    lozinka_lower = lozinka.lower()
    if "password" in lozinka_lower or "lozinka" in lozinka_lower:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return False

    sadrzi_veliko = False
    sadrzi_broj = False
    
    for znak in lozinka:
        if znak.isupper():
            sadrzi_veliko = True
        
        if znak.isdigit():
            sadrzi_broj = True

    if not sadrzi_veliko or not sadrzi_broj:
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj.")
        return False
        
    print("Lozinka je jaka!")
    return True


print("--- Provjera snage lozinke ---")
unesena_lozinka = input("Unesite lozinku za provjeru: ")

je_jaka = provjera_lozinke(unesena_lozinka)

if je_jaka:
    print("Uspješno ste postavili jaku lozinku.")
else:
    print("Postavljanje lozinke nije uspjelo zbog gore navedenih razloga.")