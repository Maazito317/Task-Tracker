from datetime import datetime
import json
import os
from typing import List, Optional
from models import Task, Status


class TaskManager:
    def __init__(self, path: str = "tasks.json"):
        self.path: str = path
        self.tasks: List[Task] = []
        self._load_tasks()

    def _load_tasks(self):
        """Load tasks from the JSON file. Create the file if it doesn't exist."""
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)
        with open(self.path, "r") as f:
            data = json.load(f)
        self.tasks = [Task.from_dict(task) for task in data]

    def _save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.path, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def _next_id(self) -> int:
        """Get the next available ID for a new task."""
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def _find_task(self, task_id: int) -> Optional[Task]:
        """Find a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def add_task(self, description: str) -> Task:
        """Add a new task."""
        new_task = Task(
            id=self._next_id(),
            description=description,
            createdAt=datetime.now(),
            updatedAt=datetime.now(),
        )
        self.tasks.append(new_task)
        self._save_tasks()
        return new_task

    def update_task(self, task_id: int, description: str) -> Task:
        """Update an existing task."""
        task = self._find_task(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found.")
        task.description = description
        task.updatedAt = datetime.now()
        self._save_tasks()
        return task

    def delete_task(self, task_id: int) -> Task:
        """Delete a task."""
        task = self._find_task(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found.")
        self.tasks.remove(task)
        self._save_tasks()
        return task

    def mark_status(self, task_id: int, status: Status):
        """Mark a task as in progress or done."""
        task = self._find_task(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found.")
        task.status = status
        task.updatedAt = datetime.now()
        self._save_tasks()
        return task

    def list_tasks(self, status: Optional[Status] = None) -> List[Task]:
        """List tasks. If status is provided, filter tasks by status."""
        if status is None:
            return self.tasks
        return [task for task in self.tasks if task.status == status]
