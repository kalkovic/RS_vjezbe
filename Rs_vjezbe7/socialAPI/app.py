from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from typing import List
from datetime import datetime

app = FastAPI()

objave = []
trenutni_id = 1


class ObjavaIn(BaseModel):
    korisnik: constr(max_length=20)
    tekst: constr(max_length=280)
    vrijeme: datetime


class Objava(ObjavaIn):
    id: int


@app.post("/objava", response_model=Objava)
def dodaj_objavu(objava: ObjavaIn):
    global trenutni_id

    nova_objava = {
        "id": trenutni_id,
        "korisnik": objava.korisnik,
        "tekst": objava.tekst,
        "vrijeme": objava.vrijeme
    }

    objave.append(nova_objava)
    trenutni_id += 1

    return nova_objava


@app.get("/objava/{id}", response_model=Objava)
def dohvati_objavu(id: int):
    for o in objave:
        if o["id"] == id:
            return o
    raise HTTPException(status_code=404, detail="Objava ne postoji")


@app.get("/korisnici/{korisnik}/objave", response_model=List[Objava])
def objave_korisnika(korisnik: str):
    return [o for o in objave if o["korisnik"] == korisnik]
