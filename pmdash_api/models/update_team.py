from typing import List, Optional
from bson import ObjectId
from models.member import Member
from pydantic import BaseModel


class UpdateTeam(BaseModel):
    name: Optional[str]
    href: Optional[str]
    bgColorClass: Optional[str]
    subTasks: Optional[List[Member]]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
