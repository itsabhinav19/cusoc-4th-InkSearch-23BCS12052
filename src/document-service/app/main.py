from fastapi import FastAPI
from app.api.document import router
from app.database.database import engine
from app.models.document import Base
from app.core.config import settings

app = FastAPI(
    title="InkSearch Document Service",
    version=settings.API_VERSION
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "service": "Document Service",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "service": "Document Service",
        "status": "healthy",
        "version": "1.0.0"
    }

Base.metadata.create_all(bind=engine)