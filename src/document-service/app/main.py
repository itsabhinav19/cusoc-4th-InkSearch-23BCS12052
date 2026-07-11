from fastapi import FastAPI
from app.api.document import router

app = FastAPI(
    title="InkSearch Document Service",
    version="1.0.0"
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
        "status": "Healthy"
    }