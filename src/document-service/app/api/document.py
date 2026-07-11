from fastapi import APIRouter, HTTPException
from app.schemas.document import DocumentCreate, Document
from app.database.fake_db import documents

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

# -----------------------------
# GET ALL DOCUMENTS
# -----------------------------
@router.get("/", response_model=list[Document])
def get_documents():
    return documents


# -----------------------------
# GET DOCUMENT BY ID
# -----------------------------
@router.get("/{document_id}", response_model=Document)
def get_document(document_id: int):

    for document in documents:
        if document.id == document_id:
            return document

    raise HTTPException(
        status_code=404,
        detail="Document not found"
    )


# -----------------------------
# CREATE DOCUMENT
# -----------------------------
@router.post("/", response_model=Document, status_code=201)
def create_document(document: DocumentCreate):

    new_document = Document(
        id=len(documents) + 1,
        **document.model_dump()
    )

    documents.append(new_document)

    return new_document


# -----------------------------
# UPDATE DOCUMENT
# -----------------------------
@router.put("/{document_id}", response_model=Document)
def update_document(document_id: int, updated_document: DocumentCreate):

    for index, document in enumerate(documents):

        if document.id == document_id:

            new_document = Document(
                id=document_id,
                **updated_document.model_dump()
            )

            documents[index] = new_document

            return new_document

    raise HTTPException(
        status_code=404,
        detail="Document not found"
    )


# -----------------------------
# DELETE DOCUMENT
# -----------------------------
@router.delete("/{document_id}")
def delete_document(document_id: int):

    for index, document in enumerate(documents):

        if document.id == document_id:

            deleted_document = documents.pop(index)

            return {
                "message": "Document deleted successfully",
                "document": deleted_document
            }

    raise HTTPException(
        status_code=404,
        detail="Document not found"
    )