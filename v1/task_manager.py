from datetime import datetime
from storage import JSONStorage

class TaskManager:
    """
    Business Logic Layer: 處理任務的增刪改查邏輯。
    """
    def __init__(self):
        self.storage = JSONStorage()

    def add_task(self, title):
        """新增任務，並自動生成 ID 與時間戳記"""
        if not title.strip():
            raise ValueError("任務標題不能為空")
            
        tasks = self.storage.load()
        new_id = max([t['id'] for t in tasks], default=0) + 1
        
        task = {
            "id": new_id,
            "title": title.strip(),
            "status": "todo",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "metadata": {} # 預留給 v2.0 的擴充欄位（前瞻性設計）
        }
        
        tasks.append(task)
        self.storage.save(tasks)
        return task

    def list_tasks(self, show_all=True):
        """回傳任務清單"""
        return self.storage.load()

    def mark_done(self, task_id):
        """根據 ID 更新任務狀態"""
        tasks = self.storage.load()
        found = False
        for t in tasks:
            if t['id'] == task_id:
                t['status'] = "done"
                found = True
                break
        
        if found:
            self.storage.save(tasks)
        return found

    def delete_task(self, task_id):
        """根據 ID 刪除任務"""
        tasks = self.storage.load()
        initial_count = len(tasks)
        tasks = [t for t in tasks if t['id'] != task_id]
        
        if len(tasks) < initial_count:
            self.storage.save(tasks)
            return True
        return False