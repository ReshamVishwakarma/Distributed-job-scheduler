from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

from app.workers.tasks import execute_job
from app.schemas.job import JobCreate, JobResponse
from app.models.job import Job, JobStatus
from app.db.deps import get_db

router = APIRouter()

@router.post("/jobs", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    new_job = Job(
        id=str(uuid4()),
        job_type=job.job_type,
        payload=job.payload,
        status=JobStatus.PENDING
    )

    # 1. Save job to DB
    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    # 2. Send job to Celery worker (NEW) - priority routing
    queue = new_job.priority
    execute_job.apply_async(
        args=[new_job.id],
        queue=queue,
        eta=new_job.run_at
    )


    # 3. Return immediately
    return new_job



@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: str, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
