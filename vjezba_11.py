def grupiraj_po_paritetu(originalna_lista):
    
    rezultat = {
        'parni': [],
        'neparni': []
    }
    
    for broj in originalna_lista:
        
        if broj % 2 == 0:
            rezultat['parni'].append(broj)
        else:
            rezultat['neparni'].append(broj)
            
    return rezultat

def unesi_listu_brojeva():
   
    unos = input("Unesite brojeve odvojene zarezom (npr. 1, 5, 8, 12): ")
    
    brojevi_liste = []
    
    elementi = unos.split(',')
    
    for element in elementi:
        cist_element = element.strip()
        
        try:
            broj = int(cist_element)
            brojevi_liste.append(broj)
        except ValueError:
            if cist_element: 
                print(f"Upozorenje: '{cist_element}' nije ispravan broj i ignoriran je.")
    
    return brojevi_liste


korisnikova_lista = unesi_listu_brojeva()

if korisnikova_lista:
    izlaz = grupiraj_po_paritetu(korisnikova_lista)

    print("\n--- Rezultat grupiranja ---")
    print(izlaz)
else:
    print("\nNije unesena nijedna ispravna lista brojeva.")