from fastapi import FastAPI
from db import CATEGORIES_DB
from models import Category

app = FastAPI(title="Category Service")

@app.get("/categories", response_model=list[Category])
def get_categories():
    return CATEGORIES_DB
