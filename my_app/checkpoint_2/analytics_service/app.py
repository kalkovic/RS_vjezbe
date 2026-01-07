from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .services import fetch_news, fetch_categories

app = FastAPI(title="Analytics Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/overview")
def overview():
    return {
        "news": fetch_news(),
        "categories": fetch_categories()
    }
