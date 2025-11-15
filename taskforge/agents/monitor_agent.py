import logging, time
logger = logging.getLogger("taskforge.monitor")

class MonitorAgent:
    def __init__(self, metrics: dict):
        self.metrics = metrics

    def watch_job(self, job_status_getter, poll_interval: float = 0.5):
        start = time.time()
        while True:
            status = job_status_getter()
            state = status.get("state")
            logger.info("Monitor sees job state: %s", state)
            self.metrics.setdefault("polls", 0)
            self.metrics["polls"] += 1
            if state in ("completed", "failed", "stopped"):
                self.metrics["runtime_seconds"] = time.time() - start
                return status
            time.sleep(poll_interval)
