from fastapi import APIRouter
from dotenv import load_dotenv, find_dotenv

import os
import models.task as task
import wrappers.mongodb as mongodb

# Used to load .env for local envion. (Dev Environments
load_dotenv(find_dotenv())

DATABASE = os.environ.get('MONGO_DATABASE')
TASKS_COLLECTION = os.environ.get('MONGO_TASKS_COLLECTION')

router = APIRouter(prefix='/tasks', tags=['Task'])


@router.post('/create')
async def create_task(task: task.Task):
    print('create', task)
    return mongodb.insert(data_base=DATABASE, collection=TASKS_COLLECTION)


@router.get('/search-by-id')
async def search_by_id(query: str):
    print('search', query)
    return mongodb.find_one(data_base=DATABASE, collection=TASKS_COLLECTION)


@router.get('/search-all')
async def search_tasks(query: str):
    print('search', query)
    return mongodb.find(data_base=DATABASE, collection=TASKS_COLLECTION)


@router.patch('/update')
async def update_task(uuid: str, patch: dict):
    print('update', uuid)
    print('patch', patch)
    return mongodb.update_one(data_base=DATABASE, collection=TASKS_COLLECTION)


@router.delete('/delete')
async def delete_task(uuid: str):
    print('delete', uuid)
    return mongodb.delete_one(data_base=DATABASE, collection=TASKS_COLLECTION)
