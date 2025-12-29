from dataclasses import dataclass

@dataclass
class NewsItem:
    def __init__(self, title, category, content):
        self.title = title
        self.category = category
        self.content = content

    @staticmethod
    def from_dict(d):
        return NewsItem(d["title"], d["category"], d["content"])

    def to_dict(self):
        return {
            "title": self.title,
            "category": self.category,
            "content": self.content
}