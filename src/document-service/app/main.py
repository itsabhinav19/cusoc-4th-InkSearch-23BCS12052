from fastapi import FastAPI

app= FastAPI(title="InkSearch Document Service")

@app.get("/")
def root():
    return{
        "service": "Document Service",
        "status": "running"
    }

@app.get("/health")
def health():
    return{
        "status": "healthy"
    }