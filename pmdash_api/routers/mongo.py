from typing import Union
from fastapi import APIRouter

import wrappers.mongodb as mongodb

router = APIRouter(tags=['Mongo'])


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get('/search')
async def read_search(search:  Union[str, None] = None):
    print('working', search)
