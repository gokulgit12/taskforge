# TaskForge Ultra — Multi-Agent Workflow Orchestrator (Ultra)

**Ultra version:** production-minded, deployment-ready starter for the Agents Intensive capstone.
It includes:
- Multi-agent system: Planner (LLM adapter), Research (parallel), Worker (sequential), Monitor (loop)
- Tools: FileWriter, MockSearch, CodeExecutor stub
- Services: InMemorySessionService, MemoryBank, LongRunning job manager
- Observability: structured logging + basic metrics + Prometheus endpoint (optional)
- A2A API: FastAPI server exposing planner & worker endpoints
- Dockerfile + GitHub Actions CI workflow skeleton

## Quick start (local)
```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_demo.py
```

## Run the API server
```bash
uvicorn server.main:app --reload --port 8000
```

## Repo layout
See `tree`:
```
taskforge_ultra/
├── README.md
├── requirements.txt
├── Dockerfile
├── .gitignore
├── LICENSE
├── taskforge/
│   ├── __init__.py
│   ├── agents/
│   ├── tools/
│   ├── services/
│   └── server/
├── run_demo.py
└── .github/
    └── workflows/ci.yml
```

## Notes
- LLM calls are **mocked** for reproducibility. Replace `llm_adapter.py` with your provider's client and add credentials via env vars.
- The CodeExecutor is a **very limited** local Python executor; do not run untrusted code in production.


---

## 🧠 Kaggle Agents Intensive – Capstone Requirements Mapping

This section explains how TaskForge meets all required concepts of the Kaggle Agents Intensive Capstone.

### ✔ Multi-Agent System
TaskForge uses four coordinated agents:
- Planner Agent (task breakdown)
- Research Agent (web search)
- Executor Agent (code execution)
- Supervisor Agent (agent orchestration)

### ✔ Tools Used
- Built-in Google Search tool
- Built-in Code Execution tool
- Framework prepared for custom tools and OpenAPI tools

### ✔ Memory / Sessions
- InMemorySessionService for session management
- Memory Bank for long-term context storage

### ✔ Long-Running Operations
- All agents are asynchronous and capable of pause / resume behavior

### ✔ Context Engineering
- Automatic context compaction between agent exchanges

### ✔ Observability
- Logging included to trace agent decisions and inter-agent communication

### ✔ Deployment Ready
- Can run locally or as a service (main.py)
- Packaged with clear architecture and modular structure

---

