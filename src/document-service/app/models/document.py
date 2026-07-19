from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255))

    author = Column(String(255))

    content = Column(Text)

    tags = Column(String(255))

    embedding = Column(Text)