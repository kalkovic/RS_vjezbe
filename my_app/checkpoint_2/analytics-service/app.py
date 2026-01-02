from fastapi import FastAPI
from services import fetch_news, fetch_categories

app = FastAPI(title="Analytics Service")

@app.get("/overview")
def overview():
    return {
        "news": fetch_news(),
        "categories": fetch_categories()
    }
