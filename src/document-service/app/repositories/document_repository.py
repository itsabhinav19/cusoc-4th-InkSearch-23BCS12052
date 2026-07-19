from __future__ import annotations

from sqlalchemy.orm import Session
from app.models.document import Document
from app.schemas.document import DocumentCreate
from app.services.embedding_service import EmbeddingService


class DocumentRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Document).all()

    @staticmethod
    def get_by_id(db: Session, document_id: int):
        return db.query(Document).filter(Document.id == document_id).first()

    embedding_service = EmbeddingService()

    @staticmethod
    def create(
        db: Session,
        document: DocumentCreate
    ):

        embedding = embedding_service.generate_embedding(
            document.content
        )

        db_document = Document(

            title=document.title,

            author=document.author,

            content=document.content,

            tags=document.tags,

            embedding=embedding
        )

        db.add(db_document)

        db.commit()

        db.refresh(db_document)

        return db_document

    @staticmethod
    def delete(db: Session, document_id: int):
        document = db.query(Document).filter(Document.id == document_id).first()
        if document:
            db.delete(document)
            db.commit()
        return document

    @staticmethod
    def update(db: Session, document_id: int, updated_document: DocumentCreate):
        document = db.query(Document).filter(Document.id == document_id).first()
        if not document:
            return None

        document.title = updated_document.title
        document.author = updated_document.author
        document.content = updated_document.content
        document.tags = updated_document.tags

        db.commit()
        db.refresh(document)
        return document
    
    @staticmethod
    def get_all(db: Session):

        return db.query(Document).all()