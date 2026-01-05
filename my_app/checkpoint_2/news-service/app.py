from fastapi import FastAPI
from .db import NEWS_DB
from .models import News

app = FastAPI(title="News Service")

@app.get("/news")
def get_all_news():
    return NEWS_DB

@app.get("/news/{news_id}")
def get_news(news_id: int):
    for n in NEWS_DB:
        if n.id == news_id:
            return n
    return {"error": "News not found"}
