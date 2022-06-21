from models.task import Task
from models.update_task import UpdateTask
from typing import Union, List
from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse
from dotenv import load_dotenv, find_dotenv
from fastapi.encoders import jsonable_encoder
from utilities.utils import create_list

import os
import wrappers.mongodb as mongodb

# Used to load .env for local envion. (Dev Environments
load_dotenv(find_dotenv())

DATABASE = os.environ.get('MONGO_DATABASE')
TASKS_COLLECTION = os.environ.get('MONGO_TASKS_COLLECTION')

router = APIRouter(prefix='/tasks', tags=['Task'])


@router.get("/fetch-all-tasks", response_description="List all tasks")
async def list_Tasks():
    tasks = await mongodb.find(data_base=DATABASE, collection=TASKS_COLLECTION, query={})
    return create_list(tasks)


@router.post('/create', response_description="Add new Project", response_model=Task)
async def create_project(task: Task = Body(...)):
    task = jsonable_encoder(task)
    new_task = await mongodb.insert(data_base=DATABASE, collection=TASKS_COLLECTION, insert_doc=task)
    created_project = await mongodb.find_one(data_base=DATABASE, collection=TASKS_COLLECTION, query={"_id": new_task.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_project)


@router.get('/search-for-task', response_description="Get a single Task", response_model=Task)
async def search_for_one(searchTerm: str, fields: list[str]):
    query = {}

    if fields is not None:
        for field in fields:
            query[field] = searchTerm

    print('search', query)
    if (task := await mongodb.find_one(data_base=DATABASE, collection=TASKS_COLLECTION, query=query)) is not None:
        return task

    raise HTTPException(status_code=404, detail=f"Task {fields} not found")


@router.get('/search-all-tasks', response_description="Get matched Tasks")
async def search_tasks(searchTerm: str, fields: list[str]):
    query = {}

    if fields is not None:
        for field in fields:
            query[field] = searchTerm

    print('search', query)
    if (tasks := await mongodb.find(data_base=DATABASE, collection=TASKS_COLLECTION, query=query)) is not None:
        return tasks

    raise HTTPException(status_code=404, detail=f"Task {fields} not found")


@router.put("/update", response_description="Update a Task", response_model=Task)
async def update_task(uuid: str, task: UpdateTask = Body(...)):
    task = {k: v for k, v in task.dict().items() if v is not None}

    if len(task) >= 1:
        update_result = await mongodb.update_one(data_base=DATABASE, collection=TASKS_COLLECTION, query={
            "_id": uuid}, update={"$set": task}),

        # if update_result.modified_count == 1:
        if (
            updated_task := await mongodb.find_one(data_base=DATABASE, collection=TASKS_COLLECTION, query={"_id": uuid})
        ) is not None:
            return updated_task

    if (existing_task := await mongodb.find_one(data_base=DATABASE, collection=TASKS_COLLECTION, query={"_id": uuid})) is not None:
        return existing_task

    raise HTTPException(status_code=404, detail=f"Task {uuid} not found")


@router.delete("/delete", response_description="Delete a Task")
async def delete_task(uuid: str):
    delete_result = await mongodb.delete_one(
        data_base=DATABASE, collection=TASKS_COLLECTION, query={"_id": uuid})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Task {uuid} not found")
