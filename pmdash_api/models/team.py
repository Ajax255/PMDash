from typing import List
from models.member import Member
from bson import ObjectId
from pydantic import BaseModel, Field
from utilities.utils import PyObjectId


class Team(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    href: str
    bgColorClass: str
    subTasks: List[Member]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
