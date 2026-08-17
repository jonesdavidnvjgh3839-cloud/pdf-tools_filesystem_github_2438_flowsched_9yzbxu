"""FlowScheduler - DAG job scheduler for Python."""

__version__ = "1.2.0"


class Scheduler:
    def __init__(self):
        self.jobs = []

    def cron(self, expr):
        def decorator(fn):
            self.jobs.append((expr, fn))
            return fn
        return decorator

    def run(self):
        return len(self.jobs)
