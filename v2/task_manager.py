from datetime import datetime
from storage import JSONStorage

class TaskManager:
    def __init__(self):
        self.storage = JSONStorage()

    def add_task(self, title, priority="Medium"):
        tasks = self.storage.load()
        new_id = max([t['id'] for t in tasks], default=0) + 1
        task = {
            "id": new_id,
            "title": title,
            "status": "todo",
            "priority": priority, # 需求 2
            "created_at": datetime.now().isoformat()
        }
        tasks.append(task)
        self.storage.save(tasks)
        return task

    def list_tasks(self, status_filter=None):
        tasks = self.storage.load()
        if status_filter: # 需求 1
            tasks = [t for t in tasks if t['status'] == status_filter]
        return tasks

    def get_task_by_id(self, task_id):
        tasks = self.storage.load()
        for t in tasks:
            if t['id'] == task_id:
                return t
        return None

    def edit_task(self, task_id, new_title=None, new_priority=None):
        tasks = self.storage.load()
        for t in tasks:
            if t['id'] == task_id:
                if new_title: t['title'] = new_title
                if new_priority: t['priority'] = new_priority
                self.storage.save(tasks)
                return True
        return False

    def delete_task(self, task_id):
        tasks = self.storage.load()
        new_tasks = [t for t in tasks if t['id'] != task_id]
        if len(new_tasks) < len(tasks):
            self.storage.save(new_tasks)
            return True
        return False

    def mark_done(self, task_id):
        tasks = self.storage.load()
        for t in tasks:
            if t['id'] == task_id:
                t['status'] = "done"
                self.storage.save(tasks)
                return True
        return False