import json

def load_news_raw():
    try:
        with open("newsapp/data/news.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []