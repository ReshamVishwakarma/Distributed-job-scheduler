from fastapi import FastAPI
from app.api.job import router as jobs_router
from app.db.init_db import init_db

app = FastAPI(title="Distributed Job Scheduler")

app.include_router(jobs_router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health_check():
    return {"status": "ok"}
