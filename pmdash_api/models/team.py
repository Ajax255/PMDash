from time import strftime
from pydantic import BaseModel


class Team(BaseModel):
    name: str
    href: str
    bgColorClass: str
