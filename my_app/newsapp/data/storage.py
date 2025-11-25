import json
import os

def load_news_raw():
    path = os.path.join("newsapp", "data", "news.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []