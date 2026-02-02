from enum import Enum

class JobStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

from uuid import uuid4
from datetime import datetime
from typing import Dict

class Job:
    def __init__(self, job_type: str, payload: Dict):
        self.id = str(uuid4())
        self.job_type = job_type
        self.payload = payload
        self.status = JobStatus.PENDING
        self.created_at = datetime.utcnow()
