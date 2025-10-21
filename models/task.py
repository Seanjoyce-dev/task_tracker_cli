from pydantic import BaseModel
from datetime import datetime

from models.status import Status


class Task(BaseModel):
    id: int
    description: str
    status: Status
    created_at: datetime
    updated_at: datetime
