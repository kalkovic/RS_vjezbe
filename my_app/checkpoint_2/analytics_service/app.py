from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI(title="Analytics Service")

NEWS_SERVICE_URL = "http://localhost:8001/news"
CATEGORY_SERVICE_URL = "http://localhost:8002/categories"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/overview")
def analytics_overview():
    news_response = requests.get(NEWS_SERVICE_URL)
    categories_response = requests.get(CATEGORY_SERVICE_URL)

    news = news_response.json()
    categories = categories_response.json()

    stats = {}

    for n in news:
        category = n.get("category", "unknown")
        stats[category] = stats.get(category, 0) + 1

    return {
        "total_news": len(news),
        "news_per_category": stats,
        "total_categories": len(categories)
    }
