from uuid import uuid4
from typing import List
from models.task import Task
from datetime import datetime
from pydantic import BaseModel


class Project(BaseModel):
    _id: str
    title: str
    application: str
    description: str
    members: List[str]
    created: datetime
    status: str
    tasks: List[Task]
    research: List[Task]
    epics: List[Task]
    stories: List[Task]
    bugs: List[Task]
    subtask: List[Task]
    inBackLog: List[Task]
    opentask: List[Task]
    closedtask: List[Task]
    inProgresstask: List[Task]
    inReviewtask: List[Task]
    testingtask: List[Task]
    blockedtask: List[Task]
