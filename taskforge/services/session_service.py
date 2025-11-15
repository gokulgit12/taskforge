import time, uuid
class InMemorySessionService:
    def __init__(self):
        self.sessions = {}
    def create(self, initial):
        sid = str(uuid.uuid4())
        self.sessions[sid] = {'created_at': time.time(), 'state': initial}
        return sid
    def get(self, sid):
        return self.sessions.get(sid)
    def update(self, sid, key, value):
        if sid in self.sessions:
            self.sessions[sid]['state'][key] = value
            return True
        return False
    def delete(self, sid):
        return self.sessions.pop(sid, None)
