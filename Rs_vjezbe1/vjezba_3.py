import random

tajni_broj = random.randint(1, 100)
broj_pokusaja = 0

print("Dobrodošao u igru pogađanja broja (1-100)!")

while True:
    
    broj_pokusaja += 1
    
    pretpostavka = int(input(f"Pokušaj #{broj_pokusaja}: Unesi broj: "))
    
    if pretpostavka < tajni_broj:
        print("Manje! Pokušaj s većim brojem.")
        
    elif pretpostavka > tajni_broj:
        print("Veće! Pokušaj s manjim brojem.")
        
    else:
        print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja!")
        break