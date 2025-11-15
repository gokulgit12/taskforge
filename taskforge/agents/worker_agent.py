import logging, time
from typing import Dict, Any
from ..tools.file_writer import FileWriterTool
from .research_agent import ResearchAgent

logger = logging.getLogger("taskforge.worker")

class WorkerAgent:
    def __init__(self, file_tool: FileWriterTool = None, research_agent: ResearchAgent = None):
        self.file_tool = file_tool or FileWriterTool()
        self.research_agent = research_agent or ResearchAgent()

    def execute_plan(self, plan: Dict[str, Any], pause_event=None, stop_event=None) -> Dict[str, Any]:
        logs = []
        steps = plan.get("steps", [])
        for i, step in enumerate(steps, start=1):
            if pause_event is not None:
                while not pause_event.is_set():
                    if stop_event and stop_event.is_set():
                        return {"logs": logs, "status": "stopped"}
                    time.sleep(0.2)
            typ = step.get("type")
            logs.append({"step": i, "id": step.get("id"), "type": typ})
            logging.info("Executing step %s (%s)", i, typ)
            if typ == "research":
                query = step.get("query", "unknown")
                res = self.research_agent.research([query])
                logs[-1]["result"] = res
            elif typ in ("compose", "decision"):
                logs[-1]["output"] = f"Auto-generated: {step.get('instruction')}"
            elif typ == "save":
                name = step.get("name", "output.json")
                path = self.file_tool.write_json(name, plan)
                logs[-1]["saved_path"] = path
            time.sleep(0.2)
        return {"logs": logs, "status": "completed"}
