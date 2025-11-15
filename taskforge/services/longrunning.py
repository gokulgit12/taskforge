import threading, time
class LongRunningJob:
    def __init__(self, job_id, target, *args, **kwargs):
        self.job_id = job_id
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._thread = threading.Thread(target=self._run_wrapper, daemon=True)
        self._pause_event = threading.Event()
        self._stop_event = threading.Event()
        self.status = {'state': 'created', 'result': None}
    def start(self):
        self._pause_event.set()
        self.status['state'] = 'running'
        self._thread.start()
    def _run_wrapper(self):
        try:
            res = self._target(self._pause_event, self._stop_event, *self._args, **self._kwargs)
            self.status['result'] = res
            if not self._stop_event.is_set():
                self.status['state'] = 'completed'
        except Exception as e:
            self.status['state'] = 'failed'
            self.status['result'] = {'error': str(e)}
    def pause(self):
        self._pause_event.clear(); self.status['state']='paused'
    def resume(self):
        self._pause_event.set(); self.status['state']='running'
    def stop(self):
        self._stop_event.set(); self.status['state']='stopped'
    def get_status(self):
        return self.status
