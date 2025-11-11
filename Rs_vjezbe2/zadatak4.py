import datetime
import math

#Zadatak 1: Automobil
print("--- ZADATAK 1 ---")

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        """Ispisuje sve atribute automobila."""
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godište: {self.godina_proizvodnje}")
        print(f"Kilometri: {self.kilometraza} km")

    def starost(self):
        """Ispisuje starost automobila."""
        trenutna_godina = datetime.date.today().year
        izracunata_starost = trenutna_godina - self.godina_proizvodnje
        print(f"Automobil je star {izracunata_starost} godina.")

moj_auto = Automobil("Volkswagen", "Golf", 2019, 85000)

moj_auto.ispis()
moj_auto.starost()

#Zadatak 2: Kalkulator
print("\n--- ZADATAK 2 ---")

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        print(f"Zbroj ({self.a} + {self.b}) = {self.a + self.b}")

    def oduzimanje(self):
        print(f"Razlika ({self.a} - {self.b}) = {self.a - self.b}")

    def mnozenje(self):
        print(f"Umnožak ({self.a} * {self.b}) = {self.a * self.b}")

    def dijeljenje(self):
        if self.b == 0:
            print("Nije moguće dijeliti s nulom!")
        else:
            print(f"Kvocijent ({self.a} / {self.b}) = {self.a / self.b}")

    def potenciranje(self):
        print(f"Potencija ({self.a} ** {self.b}) = {self.a ** self.b}")

kalk = Kalkulator(10, 5)

kalk.zbroj()
kalk.oduzimanje()
kalk.mnozenje()
kalk.dijeljenje()
kalk.potenciranje()

kalk_nula = Kalkulator(10, 0)
kalk_nula.dijeljenje()

#Zadatak 3: Student
print("\n--- ZADATAK 3 ---")

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        """Metoda koja računa prosječnu ocjenu studenta."""
        if not self.ocjene:
            return 0
        return sum(self.ocjene) / len(self.ocjene)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 19, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = []
for student_dict in studenti:
    novi_student = Student(
        student_dict['ime'],
        student_dict['prezime'],
        student_dict['godine'],
        student_dict['ocjene']
    )
    studenti_objekti.append(novi_student)

print(f"Kreirano je {len(studenti_objekti)} objekata klase Student.")

print(f"Prosjek za {studenti_objekti[0].ime}: {studenti_objekti[0].prosjek():.2f}")

najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())

print(f"Student s najvećim prosjekom je: {najbolji_student.ime} {najbolji_student.prezime} (Prosjek: {najbolji_student.prosjek():.2f})")


#Zadatak 4: Krug
print("\n--- ZADATAK 4 ---")

class Krug:
    def __init__(self, r):
        self.r = r 

    def opseg(self):
        return 2 * self.r * math.pi

    def povrsina(self):
        return (self.r ** 2) * math.pi

moj_krug = Krug(10)

print(f"Krug radijusa {moj_krug.r}")
print(f"Opseg: {moj_krug.opseg():.2f}")
print(f"Površina: {moj_krug.povrsina():.2f}")


#Zadatak 5: Radnik i Manager (Nasljeđivanje)
print("\n--- ZADATAK 5 ---")

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def rad_na_poziciji(self):
        print(f"Radnik {self.ime} radi na poziciji {self.pozicija}.")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def rad_na_poziciji(self):
        print(f"Manager {self.ime} radi na poziciji {self.pozicija} u odjelu {self.department}.")

    def give_raise(self, radnik, povecanje):
        """Povećava plaću zadanom radniku (objektu) za iznos povećanja."""
        radnik.placa += povecanje
        print(f"{self.ime} (Manager) je povisio plaću radniku {radnik.ime} za {povecanje}. Nova plaća: {radnik.placa}")

r1 = Radnik("Pero Perić", "Developer", 12000)
m1 = Manager("Ana Anić", "Team Lead", 18000, "Development")

r1.rad_na_poziciji()
m1.rad_na_poziciji()

print(f"\n--- Testiranje povišice ---")
print(f"Plaća radnika {r1.ime} PRIJE povišice: {r1.placa}")
m1.give_raise(r1, 1500)
print(f"Plaća radnika {r1.ime} NAKON povišice: {r1.placa}")