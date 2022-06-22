from typing import Union, Union, List
from bson import ObjectId
from models.task import Task
from datetime import datetime
from pydantic import BaseModel

from models.member import Member


class UpdateProject(BaseModel):
    title: Union[str, None]
    application: Union[str, None]
    description:  Union[str, None]
    description: Union[str, None]
    initials: Union[str, None]
    pinned: Union[str, None]
    bgColorClass: Union[str, None]
    members: Union[List[Member], None]
    created: Union[datetime, None]
    status: Union[str, None]
    tasks: Union[List[Task], None] = None
    research: Union[List[Task], None] = None
    epics: Union[List[Task], None] = None
    stories: Union[List[Task], None] = None
    bugs: Union[List[Task], None] = None
    subtask: Union[List[Task], None] = None
    inBackLog: Union[List[Task], None] = None
    opentask: Union[List[Task], None] = None
    closedtask: Union[List[Task], None] = None
    inProgresstask: Union[List[Task], None] = None
    inReviewtask: Union[List[Task], None] = None
    testingtask: Union[List[Task], None] = None
    blockedtask: Union[List[Task], None] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
