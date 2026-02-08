What problem am I solving?
- Running long tasks without blocking the API

What is a job?
- A unit of work executed asynchronously

Job states:
- PENDING
- RUNNING
- SUCCESS
- FAILED

Main components:
- API
- Database
- Queue
- Workers


## Day 1 Progress
- Set up FastAPI project structure
- Added health check endpoint
- Implemented job creation API
- Implemented job status retrieval API
- Currently using in-memory storage for jobs

Next:
- Replace in-memory storage with PostgreSQL

## Day 2 Progress
- Integrated PostgreSQL as persistent storage
- Added SQLAlchemy ORM setup
- Created jobs table automatically on application startup
- Replaced in-memory job storage with database-backed storage
- Verified persistence by restarting server and fetching existing jobs

Key Learnings:
- PostgreSQL permissions (database vs schema)
- Importance of Base.metadata.create_all()
- Model import order in SQLAlchemy
- FastAPI startup lifecycle

## Day 3 Progress
- Integrated Redis as a message broker
- Added Celery for background task execution
- Implemented worker-based job processing
- Connected API to async workers using task queues
- Verified end-to-end async execution and status updates

Key Learnings:
- Queue-based asynchronous system design
- Celery task registration and discovery
- Redis as a broker between API and workers
- Debugging unregistered Celery tasks
- Decoupling API layer from execution layer

## Day 4 Progress
- Added retry strategies with backoff
- Implemented idempotent job execution
- Improved failure handling and error visibility
- Strengthened job state transitions for reliability

## Day 5 – Dockerization

- Dockerized the complete distributed job scheduler
- Created a single Docker image for API and Celery worker
- Used Docker Compose to orchestrate:
  - FastAPI service
  - Celery worker
  - Redis broker
  - PostgreSQL database
- Configured environment-based DATABASE_URL and REDIS_URL
- Removed host port bindings for Redis and PostgreSQL to avoid local conflicts
- Fixed missing runtime dependencies by adding Celery and Redis to requirements.txt
- Verified end-to-end async job execution inside Docker containers

## Day 6 – Priority Queues & Scheduling

### What was implemented
- Added job priority support (high / default / low)
- Introduced scheduled jobs using `run_at`
- Configured multiple Celery queues for priority routing
- Ensured database schema initialization on API startup
- Fixed Docker startup race conditions between API and PostgreSQL
- Verified full system stability under Docker Compose

### Key Learnings
- ORM tables are created only for imported models
- Schema changes require migrations or DB resets in dev
- Docker `depends_on` does not guarantee readiness
- Health checks are required for safe service startup
- Priority queues prevent starvation of critical jobs

### Engineering Concepts Applied
- Priority-based workload isolation
- ETA-based asynchronous scheduling
- Idempotent background workers
- Distributed system startup coordination
- Production-style failure debugging

### Status
✅ Day 6 complete
