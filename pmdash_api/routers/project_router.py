from fastapi import APIRouter
from models.project import Project
from dotenv import load_dotenv, find_dotenv

import os
import wrappers.mongodb as mongodb

# Used to load .env for local envion. (Dev Environments
load_dotenv(find_dotenv())

DATABASE = os.environ.get('MONGO_DATABASE')
PROJECT_COLLECTION = os.environ.get('MONGO_PROJECT_COLLECTION')

router = APIRouter(prefix='/projects', tags=['Project'])


@router.post('/create')
async def create_project(project: Project):
    return mongodb.insert(data_base=DATABASE, collection=PROJECT_COLLECTION, insert_doc=project.dict())


@router.get('/search-for-project')
async def search_for_one(searchTerm: str, fields: list[str]):
    query = {}
    
    for field in fields:
        query[field] = searchTerm
        
    print('search', query)
    return mongodb.find_one(data_base=DATABASE, collection=PROJECT_COLLECTION, query=query)


@router.get('/search-all-projects')
async def search_projects(searchTerm: str, fields: list[str]):
    query = {}
    
    for field in fields:
        query[field] = searchTerm
        
    print('search', query)
    return mongodb.find(data_base=DATABASE, collection=PROJECT_COLLECTION, query=query)


@router.patch('/update')
async def update_project(uuid: str, patch: dict):
    query = {'_id': uuid}
    update = {"$set": patch}
    print('update', query)
    print('update', update)
    return mongodb.update_one(data_base=DATABASE, collection=PROJECT_COLLECTION, query=query, update=update)


@router.delete('/delete')
async def delete_project(uuid: str):
    query = {'_id': uuid }
    print('delete', query)
    return mongodb.delete_one(data_base=DATABASE, collection=PROJECT_COLLECTION, query=query)
