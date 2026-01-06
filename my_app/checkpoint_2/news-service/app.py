from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import NEWS_DB

app = FastAPI(title="News Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/news")
def get_all_news():
    return NEWS_DB

@app.get("/news/{news_id}")
def get_news(news_id: int):
    for n in NEWS_DB:
        if n.id == news_id:
            return n
    return {"error": "News not found"}
