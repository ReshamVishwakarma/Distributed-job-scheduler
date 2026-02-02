from fastapi import FastAPI

app = FastAPI(title="Distributed Job Scheduler")

@app.get("/health")
def health_check():
    return {"status": "ok"}
