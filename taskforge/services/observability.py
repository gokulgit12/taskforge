import logging
from prometheus_client import Counter, Gauge, generate_latest, CollectorRegistry
registry = CollectorRegistry()
JOBS_COUNTER = Counter('taskforge_jobs_total', 'Total jobs started', registry=registry)
JOB_RUNTIME = Gauge('taskforge_job_runtime_seconds', 'Last job runtime', registry=registry)
def configure_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
def metrics_endpoint():
    return generate_latest(registry)
