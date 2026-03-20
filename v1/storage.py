import json
import os

class JSONStorage:
    def __init__(self, filename="tasks.json"):
        # 取得目前檔案所在的目錄，確保 tasks.json 會跟程式放在一起
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(base_dir, filename)
        
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def load(self):
        """讀取 JSON 資料"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self, data):
        """儲存資料到 JSON"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)