from celery import Celery
import os
from kombu import Queue

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "job_worker",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

celery_app.autodiscover_tasks(["app.workers"])


celery_app.conf.task_queues = (
    Queue("high_priority"),
    Queue("default"),
    Queue("low_priority"),
)

celery_app.conf.task_default_queue = "default"

