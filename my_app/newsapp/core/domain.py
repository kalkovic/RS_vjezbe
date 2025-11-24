from dataclasses import dataclass

@dataclass
class NewsItem:
    title: str
    content: str
    category: str

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            title=d.get("title", "No title"),
            content=d.get("content", ""),
            category=d.get("category", "uncategorized")
        )

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "category": self.category
    }