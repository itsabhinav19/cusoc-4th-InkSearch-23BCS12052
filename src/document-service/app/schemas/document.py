from pydantic import BaseModel, Field, ConfigDict

class DocumentCreate(BaseModel):

    title: str = Field(..., min_length=3, max_length=255)

    author: str = Field(..., min_length=2)

    content: str = Field(..., min_length=10)

    tags: str


class DocumentUpdate(BaseModel):

    title: str = Field(..., min_length=3)

    author: str = Field(..., min_length=2)

    content: str = Field(..., min_length=10)

    tags: str


class DocumentResponse(DocumentCreate):

    id: int

    model_config = ConfigDict(from_attributes=True)