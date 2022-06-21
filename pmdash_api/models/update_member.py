from typing import Optional
from bson import ObjectId
from pydantic import BaseModel


class UpdateMember(BaseModel):
    name: Optional[str]
    handle: Optional[str]
    imageUrl: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
