from fastapi import FastAPI
from app.api.document import router
from app.database.database import engine
from app.models.document import Base

app = FastAPI(
    title="InkSearch Document Service",
    description="handles document CRUD operations",
    version="1.0.0",
    contact={
        "name": "Abhinav Kashyap"
    }
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