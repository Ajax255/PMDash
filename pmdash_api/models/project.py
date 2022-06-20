from task import Task
from uuid import uuid4
from typing import List
from datetime import datetime
from pydantic import BaseModel



class Project(BaseModel):
    uuid: uuid4
    title: str
    subject: str
    members: List[str]
    created: datetime
    status: str
    tasks: List[Task]
    research: List[Task]
    epics: List[Task]
    stories: List[Task]
    bugs: List[Task]
    subTasks: List[Task]
    inBackLog: List[Task]
    openTasks: List[Task]
    closedTasks: List[Task]
    inProgressTasks: List[Task]
    inReviewTasks: List[Task]
    testingTasks: List[Task]
    blockedTasks: List[Task]
