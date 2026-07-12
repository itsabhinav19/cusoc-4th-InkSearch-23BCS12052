from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255))

    author = Column(String(255))

    content = Column(Text)

    tags = Column(String(500))