from bson import ObjectId
from pydantic import BaseModel, Field
from utilities.utils import PyObjectId


class Member(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    handle: str = Field(...)
    imageUrl: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
