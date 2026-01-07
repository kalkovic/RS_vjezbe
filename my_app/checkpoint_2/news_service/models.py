from pydantic import BaseModel

class News(BaseModel):
    id: int
    title: str
    content: str
    category: str
