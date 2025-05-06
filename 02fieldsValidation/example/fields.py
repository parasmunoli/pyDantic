from pydantic import BaseModel, Field
from typing import List, Dict ,Optional

class Cart(BaseModel):
    userId: int
    items: List[str]
    quantities: Dict[str, int]

class Blog(BaseModel):
    title: str
    content: str
    imageUrl: Optional[str] = None

class Post(BaseModel):
    userId: str
    imageUrl: str
    caption: str = 'This is caption'
    likes: int
    comments: List[str]
