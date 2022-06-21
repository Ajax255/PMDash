from typing import List, Union
from models.project import Project
from models.update_project import UpdateProject
from fastapi import APIRouter, Body, HTTPException, Query, status
from fastapi.responses import JSONResponse
from dotenv import load_dotenv, find_dotenv
from fastapi.encoders import jsonable_encoder
from utilities.utils import create_list

import os
import wrappers.mongodb as mongodb

# Used to load .env for local envion. (Dev Environments)
load_dotenv(find_dotenv())

DATABASE = os.environ.get('MONGO_DATABASE')
PROJECT_COLLECTION = os.environ.get('MONGO_PROJECT_COLLECTION')

router = APIRouter(prefix='/projects', tags=['Project'])


@router.get("/fetch-all-projects", response_description="List all projects", response_model=List[Project])
async def list_Projects():
    projects = await mongodb.find(data_base=DATABASE, collection=PROJECT_COLLECTION, query={})
    return create_list(projects)


@router.post('/create', response_description="Add new Project", response_model=Project)
async def create_project(project: Project = Body(...)):
    project = jsonable_encoder(project)
    new_project = await mongodb.insert(data_base=DATABASE, collection=PROJECT_COLLECTION, insert_doc=project)
    created_project = await mongodb.find_one(data_base=DATABASE, collection=PROJECT_COLLECTION, query={"_id": new_project.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_project)


@router.get('/search-for-project', response_description="Get a single Project", response_model=Project)
async def search_for_one(searchTerm: str, fields: list[str] = Query(None)):
    query = {}

    if fields is not None:
        for field in fields:
            query[field] = searchTerm

    if (project := await mongodb.find_one(data_base=DATABASE, collection=PROJECT_COLLECTION, query=query)) is not None:
        return project

    raise HTTPException(status_code=404, detail=f"Project {fields} not found")


@router.get('/search-all-projects', response_description="Get matched Projects", response_model=List[Project])
async def search_projects(searchTerm: Union[str, None] = None, fields: Union[list[str], None] = None):
    query = {}

    if fields is not None:
        for field in fields:
            query[field] = searchTerm

    if (projects := await mongodb.find(data_base=DATABASE, collection=PROJECT_COLLECTION, query=query)) is not None:
        return projects

    raise HTTPException(status_code=404, detail=f"Project {fields} not found")


@router.put("/update/{uuid}", response_description="Update a Project", response_model=Project)
async def update_project(uuid: str, project: UpdateProject = Body(...)):
    project = {k: v for k, v in project.dict().items() if v is not None}

    if len(project) >= 1:
        update_result = await mongodb.update_one(data_base=DATABASE, collection=PROJECT_COLLECTION, query={"_id": uuid}, update={"$set": project}),

        # if update_result.matched_count == 1:
        if (
            updated_project := await mongodb.find_one(data_base=DATABASE, collection=PROJECT_COLLECTION, query={"_id": uuid})
        ) is not None:
            return updated_project

    if (existing_project := await mongodb.find_one(data_base=DATABASE, collection=PROJECT_COLLECTION, query={"_id": uuid})) is not None:
        return existing_project

    raise HTTPException(status_code=404, detail=f"Project {uuid} not found")


@router.delete("/delete/{uuid}", response_description="Delete a Project")
async def delete_project(uuid: str):
    delete_result = await mongodb.delete_one(data_base=DATABASE, collection=PROJECT_COLLECTION, query={"_id": uuid})

    # if delete_result.deleted_count == 1:
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content="deleted")

    # raise HTTPException(status_code=404, detail=f"Project {uuid} not found")
