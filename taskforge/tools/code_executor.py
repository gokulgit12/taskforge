import subprocess, tempfile, sys
class CodeExecutorTool:
    def run_python(self, code: str, timeout: int = 5):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            path = f.name
        try:
            res = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=timeout)
            return {'stdout': res.stdout, 'stderr': res.stderr, 'returncode': res.returncode}
        except Exception as e:
            return {'error': str(e)}
