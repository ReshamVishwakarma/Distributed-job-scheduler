from pydantic import BaseModel
from typing import Dict

class JobCreate(BaseModel):
    job_type: str
    payload: Dict

class JobResponse(BaseModel):
    id: str
    job_type: str
    payload: Dict
    status: str
    error_message: str | None = None

