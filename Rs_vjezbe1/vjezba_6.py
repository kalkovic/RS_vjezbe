# ============================================
# ZADATAK 1: Suma parnih brojeva od 1 do 100
# ============================================

print("ZADATAK 1:")

# FOR petlja
suma_for = 0
for i in range(1, 101):
    if i % 2 == 0:
        suma_for += i
print("Suma parnih brojeva (FOR):", suma_for)

# WHILE petlja
suma_while = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        suma_while += i
    i += 1
print("Suma parnih brojeva (WHILE):", suma_while)

print("-" * 40)


# =======================================================
# ZADATAK 2: Prvih 10 neparnih brojeva u obrnutom redoslijedu
# =======================================================

print("ZADATAK 2:")

# FOR petlja
neparni_for = []
for i in range(1, 20, 2):
    neparni_for.append(i)
neparni_for.reverse()
print("Neparni brojevi (FOR):", neparni_for)

# WHILE petlja
neparni_while = []
broj = 1
while len(neparni_while) < 10:
    neparni_while.append(broj)
    broj += 2
neparni_while.reverse()
print("Neparni brojevi (WHILE):", neparni_while)

print("-" * 40)

#==========================================================
#ZADATAK 3: Fibonaccijev niz
#==========================================================

# WHILE petlja
a, b = 0, 1
while a <= 1000:
    print(a)
    a, b = b, a + b
