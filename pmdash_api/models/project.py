from typing import Union, List
from bson import ObjectId
from pydantic import BaseModel, Field
from models.task import Task
from datetime import datetime
from models.member import Member
from utilities.utils import PyObjectId


class Project(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    application: str
    description: str
    initials: str
    pinned = False
    bgColorClass : str
    members: Union[List[Member], None] = []
    created:  Union[datetime, None] = None
    status: str
    tasks: Union[List[Task], None] = []
    research: Union[List[Task], None] = []
    epics: Union[List[Task], None] = []
    stories: Union[List[Task], None] = []
    bugs: Union[List[Task], None] = []
    subtask: Union[List[Task], None] = []
    inBackLog: Union[List[Task], None] = []
    opentask: Union[List[Task], None] = []
    closedtask: Union[List[Task], None] = []
    inProgresstask: Union[List[Task], None] = []
    inReviewtask: Union[List[Task], None] = []
    testingtask: Union[List[Task], None] = []
    blockedtask: Union[List[Task], None] = []

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
