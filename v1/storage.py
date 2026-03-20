import json
import os
import sys

class JSONStorage:
    """
    Data Access Layer: 負責處理所有與 JSON 檔案相關的讀寫操作。
    這種設計是為了未來 v2.0 若需更換為 SQLite 時，只需修改此模組。
    """
    def __init__(self, filename="tasks.json"):
        # 確保資料檔案跟著程式走
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(base_dir, filename)
        self._initialize_storage()

    def _initialize_storage(self):
        """初始化存儲檔案，若不存在則建立空清單"""
        if not os.path.exists(self.filename):
            try:
                with open(self.filename, 'w', encoding='utf-8') as f:
                    json.dump([], f)
            except IOError as e:
                print(f"Error: 無法初始化存儲檔案 - {e}", file=sys.stderr)

    def load(self):
        """從 JSON 讀取資料並回傳 list"""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    def save(self, data):
        """將資料序列化並寫入檔案"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error: 儲存資料失敗 - {e}", file=sys.stderr)