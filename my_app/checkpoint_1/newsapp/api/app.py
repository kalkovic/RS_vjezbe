from fastapi import FastAPI
from newsapp.core import services

app = FastAPI(title="News Aggregator API")

@app.get("/news")
def get_news(category: str | None = None):
    news = services.get_all_news()
    if category:
        news = [n for n in news if n.category == category]
    return [n.to_dict() for n in news]

@app.get("/categories")
def get_categories():
    return services.get_categories()