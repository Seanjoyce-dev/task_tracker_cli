from rich.console import Console
from rich.table import Table

from models.task import Task


def print_table(tasks: list[Task]):
    table = Table(title="Tasks list")
    table.add_column("Id")
    table.add_column("Description")
    table.add_column("Status")
    table.add_column("Created at")
    table.add_column("Updated at")

    for task in tasks:
        if task:
            formattedCreatedAt = task.created_at.strftime("%d %b, %Y")
            formattedUpdatedAt = task.updated_at.strftime("%d %b, %Y")
            table.add_row(
                str(task.id),
                task.description,
                task.status,
                formattedCreatedAt,
                formattedUpdatedAt,
            )

    console = Console()
    console.print(table)
