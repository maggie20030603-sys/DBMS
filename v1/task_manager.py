from datetime import datetime
from storage import JSONStorage

class TaskManager:
    def __init__(self):
        self.storage = JSONStorage()

    def add_task(self, title):
        """新增一個任務"""
        tasks = self.storage.load()
        new_id = max([t['id'] for t in tasks], default=0) + 1
        task = {
            "id": new_id,
            "title": title,
            "status": "todo",
            "created_at": datetime.now().isoformat()
        }
        tasks.append(task)
        self.storage.save(tasks)
        return task

    def list_tasks(self):
        """取得所有任務"""
        return self.storage.load()

    def mark_done(self, task_id):
        """標記任務為已完成"""
        tasks = self.storage.load()
        for t in tasks:
            if t['id'] == task_id:
                t['status'] = "done"
                self.storage.save(tasks)
                return True
        return False