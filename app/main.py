from fastapi import FastAPI
from app.api.job import router as jobs_router

app = FastAPI(title="Distributed Job Scheduler")

app.include_router(jobs_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
