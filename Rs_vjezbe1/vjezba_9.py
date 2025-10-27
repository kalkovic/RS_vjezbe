def ukloni_duplikate(originalna_lista):
    pomocni_skup = set(originalna_lista)
    nova_lista_bez_duplikata = list(pomocni_skup)
    return nova_lista_bez_duplikata

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
    rezultat = ukloni_duplikate(lista_za_obradu)
    print(f"Lista bez duplikata: {rezultat}")
else:
    print("Nije unesena nijedna ispravna lista brojeva.")