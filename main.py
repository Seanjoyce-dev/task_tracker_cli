from datetime import datetime
import sys

from models.command import Command
from models.status import Status
from models.task import Task
from models.tasks import Tasks


def main():
    tasks = Tasks.open_tasks()

    command = sys.argv[1]

    match command:
        case Command.ADD:

            def new_task():
                item = sys.argv[2]
                date = datetime.now()
                id = tasks.get_new_id()
                return Task(
                    id=id,
                    description=item,
                    status=Status.TODO,
                    created_at=date,
                    updated_at=date,
                )

            tasks.add_task(new_task())
            tasks.write_tasks()
            print(f"Output: Task added successfully (ID: {id})")
        case Command.UPDATE:
            pass
        case Command.DELETE:
            pass
        case Command.MARK_IN_PROGRESS:
            pass
        case Command.MARK_DONE:
            pass
        case Command.LIST:
            tasks.list_tasks()
            pass


if __name__ == "__main__":
    main()
