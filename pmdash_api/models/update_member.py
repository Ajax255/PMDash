from typing import Union
from bson import ObjectId
from pydantic import BaseModel


class UpdateMember(BaseModel):
    name: Union[str, None]
    handle: Union[str, None]
    imageUrl: Union[str, None]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
