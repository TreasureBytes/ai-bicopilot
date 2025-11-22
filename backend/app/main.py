# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="AI BI Copilot", version="0.1")

# Keep CORS permissive during dev; tighten before production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "ai-bicopilot", "version": "0.1"}

@app.post("/ingest")
async def ingest_stub():
    # placeholder: accept file uploads in next step
    return {"message": "ingest endpoint active (stub)"}
