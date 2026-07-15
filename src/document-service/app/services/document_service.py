from sqlalchemy.orm import Session

from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentCreate


class DocumentService:

    @staticmethod
    def get_documents(db: Session):
        return DocumentRepository.get_all(db)

    @staticmethod
    def get_document(db: Session, document_id: int):
        return DocumentRepository.get_by_id(db, document_id)

    @staticmethod
    def create_document(db: Session, document: DocumentCreate):
        return DocumentRepository.create(db, document)

    @staticmethod
    def delete_document(db: Session, document_id: int):
        return DocumentRepository.delete(db, document_id)
    
    @staticmethod
    def update_document(
        db: Session,
        document_id:int,
        updated_document: DocumentCreate
    ):
        return DocumentRepository.update(
            db,
            document_id,
            updated_document
        )