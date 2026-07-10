from fastapi import FastAPI
from app.api.document import router

app = FastAPI(
    title="InkSearch Document Service"
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "Running"}