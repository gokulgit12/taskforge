class MemoryBank:
    def __init__(self):
        self.store = {}
    def add(self, key, item):
        self.store.setdefault(key, []).append(item)
    def query(self, key, limit=5):
        return list(reversed(self.store.get(key, [])))[:limit]
    def compact(self, key):
        if key in self.store:
            self.store[key] = self.store[key][-10:]
