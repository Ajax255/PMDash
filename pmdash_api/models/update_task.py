from uuid import uuid4
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel


class UpdateTask(BaseModel):
    title: Optional[str]
    type: Optional[str]
    priority: Optional[str]
    lables: Optional[str]
    sprint: Optional[str]
    status: Optional[str]
    discription: Optional[str]
    attachments: Optional[List[str]]
    subTaskes: Optional[List[str]]
    assigned: Optional[str]
    created: Optional[datetime]
    subTasks: Optional[List['Task']]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
