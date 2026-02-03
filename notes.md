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
