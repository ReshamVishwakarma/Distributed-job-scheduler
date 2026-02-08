# Distributed Job Scheduling & Execution System

A backend system for asynchronous job execution using a queue-worker architecture.
Designed to handle background tasks reliably with support for retries, failure handling,
and horizontal scalability.

## Motivation
Modern applications often need to run long or heavy tasks without blocking user requests.
This project explores how real-world backend systems handle such workloads using queues
and worker-based execution.

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- Redis
- Celery
- Docker

## Architecture Overview
Client → FastAPI API → PostgreSQL → Redis Queue → Celery Workers → PostgreSQL

## Architecture Notes 
- API and worker communicate asynchronously via Redis
- PostgreSQL is used for durable job state storage
- Redis and PostgreSQL are not exposed to the host and communicate over Docker’s internal network
- The worker is idempotent and supports retries with exponential backoff


## Status
🚧 Day 1 completed: FastAPI setup and basic job APIs implemented.

(Current implementation uses in-memory storage; persistence will be added using PostgreSQL.)

🚧 Day 2 completed: Job persistence implemented using PostgreSQL and SQLAlchemy.

🚧 Day 3 completed: Asynchronous job execution implemented using Redis and Celery workers.

🚧 Day 4 completed: Reliability improvements with retries, idempotency, and failure handling.

🚧  Day 5A completed: The system is fully dockerized and runs end-to-end using Docker Compose.






## Run with Docker

### Prerequisites
- Docker
- Docker Compose (v2)

### Start the system
```bash
docker compose up --build
