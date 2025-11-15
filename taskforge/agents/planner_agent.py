import logging, json
logger = logging.getLogger("taskforge.planner")

# Simple LLM adapter abstraction (mock)
def llm_plan_mock(goal: str):
    goal_l = goal.lower()
    if "itinerary" in goal_l or "trip" in goal_l:
        return {
            "title": f"Itinerary for {goal}",
            "steps": [
                {"id": "research", "type": "research", "query": "top attractions " + goal},
                {"id": "select", "type": "decision", "instruction": "select top 3 attractions"},
                {"id": "draft", "type": "compose", "instruction": "create 3-day schedule"},
                {"id": "save", "type": "save", "name": "itinerary.json"}
            ]
        }
    return {
        "title": f"Plan for {goal}",
        "steps": [
            {"id": "analyze", "type": "research", "query": goal},
            {"id": "summarize", "type": "compose", "instruction": "Write a short summary"},
            {"id": "save", "type": "save", "name": "output.json"}
        ]
    }

class PlannerAgent:
    def __init__(self, llm_adapter=None):
        self.llm = llm_adapter or llm_plan_mock

    def create_plan(self, goal: str):
        logging.info("PlannerAgent: creating plan for goal: %s", goal)
        plan = self.llm(goal)
        return plan
