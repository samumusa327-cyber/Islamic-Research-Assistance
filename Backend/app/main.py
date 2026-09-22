
from fastapi import FastAPI

app = FastAPI(
    title="Islamic Research Assistant",
    description="AI Islamic Research Assistant",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Islamic Research Assistant API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
