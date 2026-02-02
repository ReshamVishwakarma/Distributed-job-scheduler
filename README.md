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

## High-Level Architecture

Client → API → Database → Queue → Worker


## Status
🚧 Day 1 completed: FastAPI setup and basic job APIs implemented.

(Current implementation uses in-memory storage; persistence will be added using PostgreSQL.)

