# 1️
def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])


# 2️
def maks_i_min(lista):
    maks = lista[0]
    min_ = lista[0]

    for broj in lista:
        if broj > maks:
            maks = broj
        if broj < min_:
            min_ = broj

    return (maks, min_)

#3
def presjek(skup1, skup2):
    rezultat = set()
    for element in skup1:
        if element in skup2:
            rezultat.add(element)
    return rezultat


lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [5, 10, 20, 50, 100, 3]
skup1 = {1, 2, 3, 4, 5}
skup2 = {4, 5, 6, 7, 8}

print(prvi_i_zadnji(lista1))
print(maks_i_min(lista2))
print(presjek(skup1, skup2))
