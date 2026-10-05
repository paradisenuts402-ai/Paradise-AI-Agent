from fastapi import FastAPI

app = FastAPI(title="Paradise AI Agent")


@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "Paradise AI Agent is running"
    }