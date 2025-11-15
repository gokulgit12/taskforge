import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ..agents.planner_agent import PlannerAgent
from ..agents.worker_agent import WorkerAgent
from ..services.session_service import InMemorySessionService
from ..services.longrunning import LongRunningJob
from ..services.observability import JOBS_COUNTER
import uuid

app = FastAPI(title='TaskForge Ultra API')
session_svc = InMemorySessionService()
planner = PlannerAgent()
worker = WorkerAgent()
JOB_REGISTRY = {}

class PlanRequest(BaseModel):
    goal: str
class ExecuteRequest(BaseModel):
    session_id: str
    plan: dict

@app.post('/planner')
def create_plan(req: PlanRequest):
    plan = planner.create_plan(req.goal)
    sid = session_svc.create({'goal': req.goal, 'plan': plan})
    return {'session_id': sid, 'plan': plan}

@app.post('/worker/start')
def start_worker(req: ExecuteRequest):
    sid = req.session_id
    plan = req.plan
    job_id = str(uuid.uuid4())
    job = LongRunningJob(job_id=job_id, target=worker.execute_plan, plan=plan)
    JOB_REGISTRY[job_id] = job
    JOBS_COUNTER.inc()
    job.start()
    return {'job_id': job_id, 'status': job.get_status()}

@app.post('/worker/pause/{job_id}')
def pause_worker(job_id: str):
    job = JOB_REGISTRY.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail='Job not found')
    job.pause()
    return {'job_id': job_id, 'status': job.get_status()}

@app.post('/worker/resume/{job_id}')
def resume_worker(job_id: str):
    job = JOB_REGISTRY.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail='Job not found')
    job.resume()
    return {'job_id': job_id, 'status': job.get_status()}

@app.get('/worker/status/{job_id}')
def worker_status(job_id: str):
    job = JOB_REGISTRY.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail='Job not found')
    return {'job_id': job_id, 'status': job.get_status()}
