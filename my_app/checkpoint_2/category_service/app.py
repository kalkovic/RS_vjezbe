from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import CATEGORIES_DB
from .models import Category

app = FastAPI(title="Category Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/categories", response_model=list[Category])
def get_categories():
    return CATEGORIES_DB
