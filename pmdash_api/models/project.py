from uuid import uuid4
from typing import List
from datetime import datetime
from pydantic import BaseModel

import models.task as task


class Project(BaseModel):
    uuid: str
    title: str
    subject: str
    members: List[str]
    created: datetime
    status: str
    tasks: List[task.Task]
    research: List[task.Task]
    epics: List[task.Task]
    stories: List[task.Task]
    bugs: List[task.Task]
    subtask: List[task.Task]
    inBackLog: List[task.Task]
    opentask: List[task.Task]
    closedtask: List[task.Task]
    inProgresstask: List[task.Task]
    inReviewtask: List[task.Task]
    testingtask: List[task.Task]
    blockedtask: List[task.Task]
