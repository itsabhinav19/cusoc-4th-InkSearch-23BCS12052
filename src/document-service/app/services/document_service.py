from sqlalchemy.orm import Session

from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentCreate

from app.services.embedding_service import EmbeddingService
from app.services.qdrant_service import qdrant_service

embedding_service = EmbeddingService()
class DocumentService:

    @staticmethod
    def get_documents(db: Session):
        return DocumentRepository.get_all(db)

    @staticmethod
    def get_document(db: Session, document_id: int):
        return DocumentRepository.get_by_id(db, document_id)

    @staticmethod
    def create_document(
        db: Session,
        document: DocumentCreate
    ):

    # 1. Store document in PostgreSQL
        saved_document = DocumentRepository.create(
            db,
            document
        )

    # 2. Generate embedding
        embedding = embedding_service.generate_embedding(
            saved_document.content
        )

    # 3. Store vector in Qdrant
        qdrant_service.store_document(
            document_id=saved_document.id,
            embedding=embedding,
            title=saved_document.title,
            author=saved_document.author,
            tags=saved_document.tags
        )

        return saved_document

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