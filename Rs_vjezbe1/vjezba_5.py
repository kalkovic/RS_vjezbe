try:
    broj = int(input("Unesite cijeli broj za izračun faktorijela: "))
except ValueError:
    print("Greška: Unesite ispravan cijeli broj.")
    exit()

print("\n" + "="*20)

print("REZULTAT (FOR PETLJA):")

if broj < 0:
    print("Nije definirano za negativne brojeve.")
elif broj == 0:
    print("0! = 1")
else:
    faktorijel_for = 1
    for i in range(1, broj + 1):
        faktorijel_for *= i
    print(f"{broj}! = {faktorijel_for}")

print("-" * 20)


print("REZULTAT (WHILE PETLJA):")

if broj < 0:
    print("Nije definirano za negativne brojeve.")
elif broj == 0:
    print("0! = 1")
else:
    faktorijel_while = 1
    temp_broj = broj 
    while temp_broj > 0:
        faktorijel_while *= temp_broj 
        temp_broj -= 1                
        
    print(f"{broj}! = {faktorijel_while}")

print("="*20)