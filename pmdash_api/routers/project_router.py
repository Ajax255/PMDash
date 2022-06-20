from fastapi import APIRouter
from dotenv import load_dotenv, find_dotenv

import os
import models.project as project
import wrappers.mongodb as mongodb

# Used to load .env for local envion. (Dev Environments
load_dotenv(find_dotenv())

DATABASE = os.environ.get('MONGO_DATABASE')
PROJECT_COLLECTION = os.environ.get('MONGO_PROJECT_COLLECTION')

router = APIRouter(prefix='/projects', tags=['Project'])


@router.post('/create')
async def create_project(project: project.Project):
    print('create', project)
    return mongodb.insert(data_base=DATABASE, collection=PROJECT_COLLECTION)


@router.get('/fetch-by-id')
async def search_by_id(query: str):
    print('search', query)
    return mongodb.find_one(data_base=DATABASE, collection=PROJECT_COLLECTION)


@router.get('/fetch-all')
async def search_projects(query: str):
    print('search', query)
    return mongodb.find(data_base=DATABASE, collection=PROJECT_COLLECTION)


@router.patch('/update')
async def update_project(uuid: str, patch: dict):
    print('update', uuid)
    print('patch', patch)
    return mongodb.update_one(data_base=DATABASE, collection=PROJECT_COLLECTION)


@router.delete('/delete')
async def delete_project(uuid: str):
    print('delete', uuid)
    return mongodb.delete_one(data_base=DATABASE, collection=PROJECT_COLLECTION)
