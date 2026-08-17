# FlowScheduler

A dependency-aware job scheduler for Python applications (internal codename: flowsched_9yzbxu).

## Features
- DAG-based dependency execution
- Cron-like triggers
- Retry policies
- Execution history and monitoring

## Quick Start
```python
from flowsched import Scheduler

sched = Scheduler()

@sched.cron('0 2 * * *')
def nightly_etl():
    ...
```
