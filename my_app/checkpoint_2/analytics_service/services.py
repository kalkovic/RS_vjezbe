import requests
import os

NEWS_SERVICE_URL = os.getenv("NEWS_SERVICE_URL", "http://localhost:8001")
CATEGORY_SERVICE_URL = os.getenv("CATEGORY_SERVICE_URL", "http://localhost:8002")

def fetch_news():
    try:
        r = requests.get(f"{NEWS_SERVICE_URL}/news", timeout=3)
        return r.json()
    except:
        return []

def fetch_categories():
    try:
        r = requests.get(f"{CATEGORY_SERVICE_URL}/categories", timeout=3)
        return r.json()
    except:
        return []
