from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class AuthData(BaseModel):
    username: str
    password: str

@app.get("/korisnici/{korisnik}/objave")
def get_objave(korisnik: str, auth: AuthData):
    response = requests.post(
        "http://authapi:9000/login",
        json={
            "username": auth.username,
            "password": auth.password
        }
    )

    if response.status_code != 200 or not response.json().get("authorized"):
        raise HTTPException(status_code=401, detail="Neispravni podaci")

    return {
        "korisnik": korisnik,
        "objave": [
            "Prva objava",
            "Druga objava"
        ]
    }
