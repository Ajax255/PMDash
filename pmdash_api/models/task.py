from typing import List
from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field
from utilities.utils import PyObjectId


class Task(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
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

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
