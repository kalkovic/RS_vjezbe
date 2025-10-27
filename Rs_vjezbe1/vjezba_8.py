def filtriraj_parne(originalna_lista):
    parni_brojevi = []
    
    for broj in originalna_lista:
        if broj % 2 == 0:
            parni_brojevi.append(broj)
            
    return parni_brojevi

def unesi_listu_brojeva():
    unos = input("Unesite brojeve odvojene zarezom (npr. 1, 5, 8, 12): ")
    brojevi_liste = []
    
    for element in unos.split(','):
        cist_element = element.strip()
        if cist_element.isdigit():
            brojevi_liste.append(int(cist_element))
        elif cist_element:
            print(f"Upozorenje: '{cist_element}' ignoriran.")
            
    return brojevi_liste

lista_za_obradu = unesi_listu_brojeva()

if lista_za_obradu:
    rezultat = filtriraj_parne(lista_za_obradu)
    print(f"Filtrirani parni brojevi: {rezultat}")
else:
    print("Nije unesena nijedna ispravna lista brojeva.")