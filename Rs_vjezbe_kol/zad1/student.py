from data.prilog import razredi_studenti

print(razredi_studenti)

def dohvati_studente_iz_razreda(razredi_studenti: list, naziv_razreda: str) -> list:
    lista_imena_prezimena = []
    for element in razredi_studenti:
            for student in element["element"]:
                lista_imena_prezimena.append(student["ime_prezime"])
            return lista_imena_prezimena
    
def comp_dohvati_studente_iz_razreda(razredi_studenti: list, naziv_razreda: str) -> list:
     rezultat = [element["razred"] 
                 for element in razredi_studenti 
                 for student in element ["studenti"]
                 if element["razred"] == naziv_razreda]
     return rezultat
     #expression element in iterable for element_2 in iterable2

def prosjek_studenta(razredi_studenti: list, ime_prezime: str) -> float :
    for element in razredi_studenti:
         for student in element["studenti"]:
              if student["ime_prezime"] == ime_prezime:
                for kolegij in student["kolegiji"]:
                     sum += kolegij["ocjena"]
                     prosjek = sum/(student["kolegiji"])
                return round(prosjek, 1)
              
def comp_prosjek_studenta(razredi_studenti: list, ime_prezime: str) -> float:
     student = [sum(kolegiji["ocjena"], )
          for element in  razredi_studenti       
          element for element in razredi_studenti 
          for student in element["studenti"] 
          if student["ime_prezime"] == ime_prezime]
     
return student
#print(prosjek_studenta(razredi_studenti, "Ana Horvat"))
#print(dohvati_studente_iz_razreda(razredi_studenti, "1B"))

#print(comp_dohvati_studente_iz_razreda(razredi_studenti, "1A"))

rezultat = [(, len element["studenti"])]