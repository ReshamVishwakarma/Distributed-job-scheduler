from sqlalchemy import Column, String, JSON, DateTime
from sqlalchemy.sql import func
from app.db.database import Base
from enum import Enum
from sqlalchemy import Column, String, DateTime
from datetime import datetime

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
    status = Column(String)
    priority = Column(String, default="default")   # NEW
    run_at = Column(DateTime, nullable=True)        # NEW
    error_message = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)