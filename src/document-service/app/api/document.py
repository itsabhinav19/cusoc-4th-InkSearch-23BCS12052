from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.document import Document
from app.schemas.document import DocumentCreate
from app.schemas.document import DocumentResponse

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/", response_model=list[DocumentResponse])
def get_documents(db: Session = Depends(get_db)):

    return db.query(Document).all()


@router.post("/", response_model=DocumentResponse)
def create_document(
        document: DocumentCreate,
        db: Session = Depends(get_db)
):

    db_document = Document(**document.model_dump())

    db.add(db_document)

    db.commit()

    db.refresh(db_document)

    return db_document