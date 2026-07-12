from typing import List
from pydantic import BaseModel

class DocumentCreate(BaseModel):

    title: str

    author: str

    content: str

    tags: str


class DocumentResponse(DocumentCreate):

    id: int

    class Config:
        from_attributes = True