from pydantic import BaseModel
from typing import List

class DocumentCreate(BaseModel):
    title: str
    author: str
    content: str
    tags: List[str] = []

class Document(DocumentCreate):
    id: int