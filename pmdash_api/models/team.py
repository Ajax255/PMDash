from time import strftime
from pydantic import BaseModel


class Team(BaseModel):
    uuid: str
    name: str
    href: str
    bgColorClass: str
