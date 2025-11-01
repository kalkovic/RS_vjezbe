def prvi_i_zadnji(lista):
    return lista[0], lista[-1]

def maks_i_min(lista):
    maks = lista[0]
    min = lista[0]
    for x in lista:
        if x > maks:
            maks = x
        if x < min:
            min = x
    return maks, min

def presjek(s1, s2):
    novi = set()
    for x in s1:
        if x in s2:
            novi.add(x)
    return novi

lista = [1, 2, 3, 4, 5, 6]
brojevi = [5, 10, 20, 50, 100, 3]
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(prvi_i_zadnji(lista))
print(maks_i_min(brojevi))
print(presjek(s1, s2))
