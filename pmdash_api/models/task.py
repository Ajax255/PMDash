from uuid import uuid4
from typing import List
from datetime import datetime
from pydantic import BaseModel


class Task(BaseModel):
    _id: str
    title: str
    type: str
    priority: str
    lables: str
    sprint: str
    status: str
    discription: str
    attachments: List[str]
    subTaskes: List[str]
    assigned: str
    created: datetime
    subTasks: List['Task']
