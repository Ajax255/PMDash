from time import strftime
from typing import List
from models.member import Member
from pydantic import BaseModel


class Team(BaseModel):
    _id: str
    name: str
    href: str
    bgColorClass: str
    subTasks: List[Member]
