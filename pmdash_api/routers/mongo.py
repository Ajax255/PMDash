from typing import Union
from fastapi import APIRouter

import wrappers.mongodb as mongodb

router = APIRouter(tags=['Mongo'])


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.post('/create')
async def read_search(payload):
    print('create', payload)


@router.get('/search')
async def read_search(search:  Union[str, None] = None):
    print('search', search)


@router.get('/update')
async def read_search(ids:  Union[str, list[str], None] = None):
    print('update', ids)


@router.get('/delete')
async def read_search(ids:  Union[str, list[str], None] = None):
    print('delete', ids)
