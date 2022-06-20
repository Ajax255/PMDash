from pydantic import BaseModel


class Memeber(BaseModel):
    uuid: str
    name: str
    handle: str
    imageUrl: str
