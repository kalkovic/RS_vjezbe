import math
# 1. List comprehension - Parni kvadrati
parni_kvadrati = [x**2 for x in range(20, 51) if (x**2) % 2 == 0]

print(f"1. parni_kvadrati = {parni_kvadrati}")


# 2. List comprehension - Duljina riječi sa slovom 'a'
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "cokolada", "ples", "pjesma", "otorinolaringolog"]

duljine_sa_slovom_a = [len(rijec) for rijec in rijeci if 'a' in rijec]

print(f"2. duljine_sa_slovom_a = {duljine_sa_slovom_a}")


# 3. Dictionary comprehension - Kubovi, parni i neparni brojevi
kubovi = {x: x**3 if x % 2 != 0 else x for x in range(1, 11)}

print(f"3. kubovi = {kubovi}")

# 4. Dictionary comprehension - Korijeni, iteracija s korakom 50
korijeni = {x: round(x**0.5, 2) for x in range(50, 501, 50)}

print(f"4. korijeni = {korijeni}")

# 5. List comprehension - Rječnici sa zbrojem bodova
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]

zbrojeni_bodovi = [{student['prezime']: sum(student['bodovi'])} for student in studenti]

print(f"5. zbrojeni_bodovi = {zbrojeni_bodovi}")

# 6. Dictionary comprehension - Liste faktorijela
faktori = {n: [math.factorial(i) for i in range(1, n + 1)] for n in range(1, 11)}

print(f"6. faktori = {faktori}")