from fastapi import APIRouter, HTTPException
from app.models.job import Job
from app.schemas.job import JobCreate, JobResponse

router = APIRouter()

# Temporary in-memory store
jobs_store = {}

@router.post("/jobs", response_model=JobResponse)
def create_job(job: JobCreate):
    new_job = Job(job_type=job.job_type, payload=job.payload)
    jobs_store[new_job.id] = new_job

    return JobResponse(
        id=new_job.id,
        job_type=new_job.job_type,
        payload=new_job.payload,
        status=new_job.status
    )

@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: str):
    job = jobs_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return JobResponse(
        id=job.id,
        job_type=job.job_type,
        payload=job.payload,
        status=job.status
    )
