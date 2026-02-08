from pydantic import BaseModel
from typing import Dict
from datetime import datetime
from typing import Optional

class JobCreate(BaseModel):
    job_type: str
    payload: dict
    priority: Optional[str] = "default"   # high | default | low
    run_at: Optional[datetime] = None

class JobResponse(BaseModel):
    id: str
    job_type: str
    payload: Dict
    status: str
    error_message: str | None = None
    priority: str
    run_at: Optional[datetime]


