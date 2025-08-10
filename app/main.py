from fastapi import FastAPI
from pymongo import MongoClient, errors
import os

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Метрики Prometheus на /metrics
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

client = MongoClient(os.getenv("MONGO_URL", "mongodb://mongo:27017/app"),
                     serverSelectionTimeoutMS=800)
db = client.get_database()

@app.get("/healthz")
def healthz():
    try:
        db.command("ping")
        return {"status": "ok", "mongo": "ok"}
    except errors.PyMongoError:
        return {"status": "degraded", "mongo": "down"}
