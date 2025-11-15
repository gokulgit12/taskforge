import os, json
class FileWriterTool:
    def __init__(self, base_dir='artifacts'):
        os.makedirs(base_dir, exist_ok=True)
        self.base_dir = base_dir
    def write_json(self, name, data):
        path = f"{self.base_dir}/{name}"
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        return path
