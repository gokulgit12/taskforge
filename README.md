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

If you want, I can:
- Replace mocks with OpenAI adapter and show secure env var usage.
- Add Redis-backed sessions and memory.
- Add Prometheus + Grafana demo.
