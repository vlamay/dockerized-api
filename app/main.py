from fastapi import FastAPI
from pymongo import MongoClient
import os
app = FastAPI()
client = MongoClient(os.getenv("MONGO_URL","mongodb://mongo:27017/app"))
db = client.get_database()
@app.get("/healthz")
def healthz():
    db.command("ping"); return {"status":"ok"}
