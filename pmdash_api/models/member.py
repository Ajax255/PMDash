from pydantic import BaseModel


class Member(BaseModel):
    _id: str
    name: str
    handle: str
    imageUrl: str
