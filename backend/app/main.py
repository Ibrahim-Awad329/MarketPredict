from fastapi import FastAPI
from app.utils.logging import setup_logging
from app.database.db import engine, Base

setup_logging()
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MarketPredict API", version="1.0.0")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"}
