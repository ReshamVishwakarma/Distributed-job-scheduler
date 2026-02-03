from sqlalchemy import Column, String, JSON, DateTime
from sqlalchemy.sql import func
from app.db.database import Base
from enum import Enum

class JobStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, index=True)
    job_type = Column(String, index=True)
    payload = Column(JSON)
    status = Column(String, default=JobStatus.PENDING)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
