import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..tools.search_tool import MockSearchTool
logger = logging.getLogger("taskforge.research")

class ResearchAgent:
    def __init__(self, search_tool=None, max_workers=4):
        self.search_tool = search_tool or MockSearchTool()
        self.pool = ThreadPoolExecutor(max_workers=max_workers)

    def research(self, queries):
        futures = {self.pool.submit(self.search_tool.call, q): q for q in queries}
        results = {}
        for fut in as_completed(futures):
            q = futures[fut]
            try:
                res = fut.result()
            except Exception as e:
                logger.exception("Search failed for %s", q)
                res = [{"error": str(e)}]
            results[q] = res
        return results
