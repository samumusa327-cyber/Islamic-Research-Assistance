

from fastapi import FastAPI

app = FastAPI(
    title="Islamic Research Assistance"
)

@app.get("/")
def home():
    return {
        "message": "Barka da zuwa Islamic Research Assistance",
        "status": "Aiki yana gudana"
    }

@app.get("/about")
def about():
    return {
        "name": "Islamic Research Assistance",
        "language": "Hausa"
    }
