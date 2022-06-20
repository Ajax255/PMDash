from fastapi import APIRouter
from models.task import Task
from dotenv import load_dotenv, find_dotenv

import os
import wrappers.mongodb as mongodb

# Used to load .env for local envion. (Dev Environments
load_dotenv(find_dotenv())

DATABASE = os.environ.get('MONGO_DATABASE')
TASKS_COLLECTION = os.environ.get('MONGO_TASKS_COLLECTION')

router = APIRouter(prefix='/tasks', tags=['Task'])


@router.post('/create')
async def create_task(task: Task):
    print('create', task)
    return mongodb.insert(data_base=DATABASE, collection=TASKS_COLLECTION, insert_doc=task.dict())


@router.get('/search-for-task')
async def search_for_one(searchTerm: str, fields: list[str]):
    query = {}

    for field in fields:
        query[field] = searchTerm

    print('search', query)
    return mongodb.find_one(data_base=DATABASE, collection=TASKS_COLLECTION, query=query)


@router.get('/search-all-tasks')
async def search_tasks(searchTerm: str, fields: list[str]):
    query = {}

    for field in fields:
        query[field] = searchTerm

    print('search', query)
    return mongodb.find(data_base=DATABASE, collection=TASKS_COLLECTION, query=query)


@router.patch('/update')
async def update_task(uuid: str, patch: dict):
    query = {'_id': uuid}
    update = {"$set": patch}
    print('update', query)
    print('update', update)
    return mongodb.update_one(data_base=DATABASE, collection=TASKS_COLLECTION, query=query, update=update)


@router.delete('/delete')
async def delete_task(uuid: str):
    query = {'_id': uuid}
    print('delete', query)
    return mongodb.delete_one(data_base=DATABASE, collection=TASKS_COLLECTION, query=query)
