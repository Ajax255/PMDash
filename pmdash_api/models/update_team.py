from typing import List,  Union
from bson import ObjectId
from models.member import Member
from pydantic import BaseModel


class UpdateTeam(BaseModel):
    name:  Union[str, None]
    bgColorClass:  Union[str, None]
    members: Union[List[Member], None] 

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
