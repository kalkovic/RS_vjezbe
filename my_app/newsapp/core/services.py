from ..data.storage import load_news_raw
from .domain import NewsItem
from typing import List

def get_all_news() -> List[NewsItem]:
    raw = load_news_raw()
    return [NewsItem.from_dict(r) for r in raw]

def get_categories() -> List[str]:
    raw = load_news_raw()
    cats = sorted({r.get("category", "uncategorized") for r in raw})
    return cats

def get_news_by_category(category: str) -> List[NewsItem]:
    return [n for n in get_all_news() if n.category == category]
