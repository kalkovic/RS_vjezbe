#1
def isPrime(broj):
    if broj <= 1:
        return False
    
    for i in range(2, broj):
        if broj % i == 0:
            return False
    
    return True

#2
def primes_in_range(start, end):
    prosti = []
    
    for broj in range(start, end + 1):
        if isPrime(broj):
            prosti.append(broj)
    
    return prosti

# -----------------------------
# Unos korisnika za 1. zadatak
# -----------------------------
broj = int(input("Unesite cijeli broj za provjeru: "))

if isPrime(broj):
    print(f"{broj} je prost broj ✅")
else:
    print(f"{broj} nije prost broj ❌")


# -----------------------------
# Unos korisnika za 2. zadatak
# -----------------------------
start = int(input("Unesite početak raspona: "))
end = int(input("Unesite kraj raspona: "))

prosti_brojevi = primes_in_range(start, end)

print(f"Prosti brojevi u rasponu {start}-{end}: {prosti_brojevi}")
