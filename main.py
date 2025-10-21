from datetime import datetime
import typer
from typing_extensions import Annotated

from models.status import Status
from models.task import Task
from models.tasks import Tasks

tasks = Tasks.create()
app = typer.Typer()


@app.command()
def add(description: str):
    date = datetime.now()
    id = tasks.get_new_id()
    task = Task(
        id=id,
        description=description,
        status=Status.TODO,
        created_at=date,
        updated_at=date,
    )

    tasks.add_task(task)
    tasks.write_tasks()
    print(f"Output: Task added successfully (ID: {id})")


@app.command()
def update(id: int, description: str):
    updated = tasks.update_task(id, description=description)
    if updated:
        tasks.write_tasks()
        print("Task was successfully updated")
    else:
        print(f"Cound not find task with id of {id}")


@app.command()
def delete(id: int):
    tasks.delete_task(id)
    tasks.write_tasks()


@app.command()
def mark_in_progress(id: int):
    updated = tasks.update_task_status(id, status=Status.IN_PROGRESS)
    if updated:
        tasks.write_tasks()
        print("Task was successfully updated")
    else:
        print(f"Cound not find task with id of {id}")


@app.command()
def mark_done(id: int):
    updated = tasks.update_task_status(id, status=Status.DONE)
    if updated:
        tasks.write_tasks()
        print("Task was successfully updated")
    else:
        print(f"Cound not find task with id of {id}")


@app.command()
def list(status: Annotated[Status | None, typer.Argument()] = None):
    if status:
        tasks.list_filtered_tasks(status=status)
    else:
        tasks.list_tasks()


if __name__ == "__main__":
    app()
