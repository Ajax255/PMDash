from typing import List
from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field
from utilities.utils import PyObjectId


class Task(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    type: str = Field(...)
    priority: str = Field(...)
    lables: str = Field(...)
    sprint: str = Field(...)
    status: str = Field(...)
    discription: str = Field(...)
    attachments: List[str] = Field(...)
    subTaskes: List[str] = Field(...)
    assigned: str = Field(...)
    created: datetime = Field(...)
    subTasks: List['Task'] = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
