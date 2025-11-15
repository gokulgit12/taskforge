from taskforge.agents.planner_agent import PlannerAgent
def test_planner():
    p = PlannerAgent()
    plan = p.create_plan('short trip')
    assert 'steps' in plan
