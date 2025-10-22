from datetime import datetime
from pathlib import Path
from table_builder import print_table

from pydantic import BaseModel, Field
import json

from models.status import Status
from models.task import Task

DEFAULT_TASKS_FILE = Path(Path.cwd() / "tasks.json")


class Tasks(BaseModel):
    items: list[Task] = Field(default_factory=list)

    def add_task(self, task: Task):
        self.items.append(task)

    def update_task(self, id: int, description: str) -> bool:
        task = self.find(id)
        if task:
            task.description = description
            task.updated_at = datetime.now()
            return True

        return False

    def update_task_status(self, id: int, status: Status) -> bool:
        task = self.find(id)
        if task:
            task.updated_at = datetime.now()
            task.status = status
            return True

        return False

    def delete_task(self, id: int) -> bool:
        before = len(self.items)
        self.items = [task for task in self.items if id != task.id]
        return len(self.items) < before

    def list_tasks(self):
        print_table(self.items)

    def list_filtered_tasks(self, status: Status):
        filteredList = [task for task in self.items if status == task.status]
        print_table(filteredList)

    def find(self, id: int) -> Task | None:
        return next((t for t in self.items if t.id == id), None)

    def next_id(self) -> int:
        return max((t.id for t in self.items), default=0) + 1

    def write_tasks(self):
        with open(DEFAULT_TASKS_FILE, "w") as f:
            f.write(self.model_dump_json(indent=2))

    @classmethod
    def create(cls) -> Tasks:
        with open(DEFAULT_TASKS_FILE, "r") as f:
            data = json.load(f)
            if data:
                return Tasks(**data)
            else:
                return Tasks()
