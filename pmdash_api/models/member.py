from pydantic import BaseModel


class Memeber(BaseModel):
    name: str
    handle: str
    imageUrl: str
