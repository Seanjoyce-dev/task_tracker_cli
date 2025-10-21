from datetime import datetime

from pydantic import BaseModel, Field
import json

from models.status import Status
from models.task import Task


class Tasks(BaseModel):
    items: list[Task] = Field(default_factory=list)

    def add_task(self, task: Task):
        self.items.append(task)

    def update_task(self, id: int, description: str) -> bool:
        updated = False
        for task in self.items:
            if task.id == id:
                task.description = description
                task.updated_at = datetime.now()
                updated = True

        return updated

    def update_task_status(self, id: int, status: Status) -> bool:
        updated = False
        for task in self.items:
            if task.id == id:
                task.updated_at = datetime.now()
                task.status = status
                updated = True

        return updated

    def delete_task(self, id: int):
        self.items = [task for task in self.items if id != task.id]

    def list_tasks(self):
        for task in self.items:
            print(task)

    def list_filtered_tasks(self, status: Status):
        for task in self.items:
            if task.status == status:
                print(task)

    def get_new_id(self) -> int:
        if len(self.items) > 0:
            return max(self.items, key=lambda x: x.id).id + 1
        else:
            return 1

    def write_tasks(self):
        with open("./tasks.json", "w") as f:
            f.write(self.model_dump_json(indent=2))

    @classmethod
    def create(cls) -> Tasks:
        with open("./tasks.json", "r") as f:
            data = json.load(f)
            if data:
                return Tasks(**data)
            else:
                return Tasks()
