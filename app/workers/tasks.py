import time
from app.workers.celery_app import celery_app
from app.db.database import SessionLocal
from app.models.job import Job, JobStatus


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3, "countdown": 5})
def execute_job(self, job_id: str):
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            return "Job not found"

        job.status = JobStatus.RUNNING
        db.commit()

        # Simulate work
        time.sleep(5)

        job.status = JobStatus.SUCCESS
        db.commit()

        return "Job completed"
    except Exception as e:
        job.status = JobStatus.FAILED
        db.commit()
        raise e
    finally:
        db.close()
