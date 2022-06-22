from typing import List, Union
from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel


class UpdateTask(BaseModel):
    title: Union[str, None]
    type: Union[str, None]
    priority: Union[str, None]
    lables: Union[str, None]
    sprint: Union[str, None]
    status: Union[str, None]
    discription: Union[str, None]
    attachments: Union[List[str], None]
    subTaskes: Union[List[str], None]
    assigned: Union[str, None]
    created: Union[datetime, None]
    subTasks: Union[List['UpdateTask'], None]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
