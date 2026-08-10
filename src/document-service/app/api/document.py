from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.document import DocumentCreate, DocumentResponse, DocumentUpdate
from app.services.document_service import DocumentService

from app.schemas.search import SearchRequest
from app.services.search_service import SearchService
from app.repositories.document_repository import DocumentRepository
from app.services.hybrid_search_service import HybridSearchService

# from app.repositories.search_repository import SearchRepository

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/", response_model=list[DocumentResponse])
def get_documents(db: Session = Depends(get_db)):
    return DocumentService.get_documents(db)


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int, db: Session = Depends(get_db)):

    document = DocumentService.get_document(db, document_id)

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    return document


@router.post("/{document_id}/embed")
def generate_embedding(
        document_id: int,
        db: Session = Depends(get_db)
):

    document = DocumentService.generate_embedding(
        db,
        document_id
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return {
        "message": "Embedding generated"
    }


@router.delete("/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):

    document = DocumentService.delete_document(db, document_id)

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    return {
        "message": "Document deleted successfully"
    }

@router.put(
    "/{document_id}",
    response_model=DocumentResponse
)
def update_document(
    document_id: int,
    updated_document: DocumentUpdate,
    db: Session = Depends(get_db)
):

    document = DocumentService.update_document(
        db,
        document_id,
        updated_document
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return document

@router.post("/search")
def search_documents(
    request: SearchRequest,
    db: Session = Depends(get_db)
):

    results = SearchService.semantic_search(
        request.query,
        request.top_k
    )

    return results[:request.top_k]

@router.post("/hybrid-search")
def hybrid_search(
    request: SearchRequest,
    db: Session = Depends(get_db)
):

    return HybridSearchService.hybrid_search(
        db=db,
        query=request.query,
        top_k=request.top_k
    )