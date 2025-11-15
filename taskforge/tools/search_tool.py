import time
class MockSearchTool:
    def call(self, query: str, top_k: int = 3):
        time.sleep(0.2)
        return [{'title': f'Result {i+1} for {query}', 'snippet': f'Snippet {i+1}'} for i in range(top_k)]
