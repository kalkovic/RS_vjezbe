def brojanje_riječi(tekst):
    
    tekst_za_obradu = tekst.lower()
    riječi = tekst_za_obradu.split()
    
    brojač_riječi = {}
    
    for riječ in riječi:
        
        if riječ.endswith('.') or riječ.endswith(','):
            riječ = riječ[:-1]
            
        
        if riječ in brojač_riječi:
            brojač_riječi[riječ] += 1
        else:
            brojač_riječi[riječ] = 1
            
    return brojač_riječi

tekst_od_korisnika = input("Unesite tekst za brojanje riječi: ")

print(brojanje_riječi(tekst_od_korisnika))