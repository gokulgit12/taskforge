import logging, uuid
from taskforge.agents.planner_agent import PlannerAgent
from taskforge.agents.research_agent import ResearchAgent
from taskforge.agents.worker_agent import WorkerAgent
from taskforge.agents.monitor_agent import MonitorAgent
from taskforge.tools.file_writer import FileWriterTool
from taskforge.services.longrunning import LongRunningJob
from taskforge.services.observability import configure_logging
configure_logging()
logging.info('Starting demo')
def worker_target(pause_event, stop_event, plan, worker):
    return worker.execute_plan(plan, pause_event=pause_event, stop_event=stop_event)
def main():
    planner = PlannerAgent()
    research = ResearchAgent()
    file_tool = FileWriterTool()
    worker = WorkerAgent(file_tool=file_tool, research_agent=research)
    monitor = MonitorAgent({})
    goal = 'Plan a weekend trip to Goa'
    plan = planner.create_plan(goal)
    print('Plan:', plan)
    job_id = str(uuid.uuid4())
    job = LongRunningJob(job_id=job_id, target=worker_target, plan=plan, worker=worker)
    job.start()
    status = monitor.watch_job(job.get_status)
    print('Job finished with status:', status)
if __name__ == '__main__':
    main()
