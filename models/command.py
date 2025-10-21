from enum import Enum

class Command(str, Enum):
    ADD = "add"
    UPDATE = "update"
    DELETE = "delete"
    MARK_IN_PROGRESS = "mark_in_progress"
    MARK_DONE = "mark_done"
    LIST = "list"
