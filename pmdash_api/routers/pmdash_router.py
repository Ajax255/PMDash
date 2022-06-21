from models.team import Team
from models.update_team import UpdateTeam
from typing import Union, List
from models.member import Member
from models.update_member import UpdateMember
from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse
from dotenv import load_dotenv, find_dotenv
from fastapi.encoders import jsonable_encoder
from utilities.utils import create_list

import os
import wrappers.mongodb as mongodb

# Used to load .env for local envion. (Dev Environments)
load_dotenv(find_dotenv())

DATABASE = os.environ.get('MONGO_DATABASE')
MEMBERS_COLLECTION = os.environ.get('MONGO_MEMBERS_COLLECTION')
TEAMS_COLLECTION = os.environ.get('MONGO_TEAMS_COLLECTION')

router = APIRouter(prefix='/pmdash', tags=['PMDash'])


# member endpoints
@router.get("/fetch-all-members", response_description="List all members", response_model=List[Member])
async def list_Members():
    members = await mongodb.find(data_base=DATABASE, collection=MEMBERS_COLLECTION, query={})
    return create_list(members)


@router.post('/create-member', response_description="Add new Member", response_model=Member)
async def create_member(member: Member = Body(...)):
    member = jsonable_encoder(member)
    new_member = await mongodb.insert(data_base=DATABASE, collection=MEMBERS_COLLECTION, insert_doc=member)
    created_member = await mongodb.find_one(data_base=DATABASE, collection=MEMBERS_COLLECTION, query={"_id": new_member.inserted_id})
    print('create', member)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_member)


@router.get('/search-for-member', response_description="Get a single Member", response_model=Member)
async def search_for_one_member(searchTerm: str, fields: list[str]):
    query = {}

    if fields is not None:
        for field in fields:
            query[field] = searchTerm

    print('search', query)
    if (member := await mongodb.find_one(data_base=DATABASE, collection=MEMBERS_COLLECTION, query=query)) is not None:
        return member

    raise HTTPException(status_code=404, detail=f"Member {fields} not found")


@router.get('/search-all-members', response_description="Get matched Members", response_model=List[Member])
async def search_all_members(searchTerm: Union[str, None] = None, fields: Union[list[str], None] = None):
    query = {}

    if fields is not None:
        for field in fields:
            query[field] = searchTerm

    print('search', query)
    if (members := await mongodb.find(data_base=DATABASE, collection=MEMBERS_COLLECTION, query=query)) is not None:
        return members

    raise HTTPException(status_code=404, detail=f"Member {fields} not found")


@router.put("/update-member", response_description="Update a Member", response_model=Member)
async def update_member(uuid: str, member: UpdateMember = Body(...)):
    member = {k: v for k, v in member.dict().items() if v is not None}

    if len(member) >= 1:
        update_result = await mongodb.update_one(data_base=DATABASE, collection=MEMBERS_COLLECTION, query={
            "_id": uuid}, update={"$set": member}),

        # if update_result.modified_count == 1:
        if (
            updated_member := await mongodb.find_one(data_base=DATABASE, collection=MEMBERS_COLLECTION, query={"_id": uuid})
        ) is not None:
            return updated_member

    if (existing_member := await mongodb.find_one(data_base=DATABASE, collection=MEMBERS_COLLECTION, query={"_id": uuid})) is not None:
        return existing_member

    raise HTTPException(status_code=404, detail=f"Member {uuid} not found")


@router.delete("/delete-member", response_description="Delete a Member")
async def delete_member(uuid: str):
    delete_result = await mongodb.delete_one(
        data_base=DATABASE, collection=MEMBERS_COLLECTION, query={"_id": uuid})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Member {uuid} not found")


# team endpoints
@router.get("/fetch-all-teams", response_description="List all teams")
async def list_Teams():
    teams = await mongodb.find(data_base=DATABASE, collection=TEAMS_COLLECTION, query={})
    return create_list(teams)


@router.post('/create-team', response_description="Add new Team", response_model=Team)
async def create_team(team: Team = Body(...)):
    team = jsonable_encoder(team)
    new_team = await mongodb.insert(data_base=DATABASE, collection=TEAMS_COLLECTION, insert_doc=team)
    created_team = await mongodb.find_one({"_id": new_team.inserted_id})
    print('create', team)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_team)


@router.get('/search-for-team', response_description="Get a single Team", response_model=Team)
async def search_for_one_team(searchTerm: str, fields: list[str]):
    query = {}

    if fields is not None:
        for field in fields:
            query[field] = searchTerm

    print('search', query)
    if (team := await mongodb.find_one(data_base=DATABASE, collection=TEAMS_COLLECTION, query=query)) is not None:
        return team

    raise HTTPException(status_code=404, detail=f"Team {fields} not found")


@router.get('/search-all-teams', response_description="Get matched Teams", response_model=List[Team])
async def search_all_teams(searchTerm: Union[str, None] = None, fields: Union[list[str], None] = None):
    query = {}

    if fields is not None:
        for field in fields:
            query[field] = searchTerm

    print('search', query)
    if (teams := await mongodb.find(data_base=DATABASE, collection=TEAMS_COLLECTION, query=query)) is not None:
        return teams

    raise HTTPException(status_code=404, detail=f"Team {fields} not found")


@router.put("/update-team", response_description="Update a Team", response_model=Team)
async def update_team(uuid: str, team: UpdateTeam = Body(...)):
    team = {k: v for k, v in team.dict().items() if v is not None}

    if len(team) >= 1:
        update_result = await mongodb.update_one(data_base=DATABASE, collection=TEAMS_COLLECTION, query={
            "_id": uuid}, update={"$set": team}),

        # if update_result.modified_count == 1:
        if (
            updated_team := await mongodb.find_one(data_base=DATABASE, collection=TEAMS_COLLECTION, query={"_id": uuid})
        ) is not None:
            return updated_team

    if (existing_team := await mongodb.find_one(data_base=DATABASE, collection=TEAMS_COLLECTION, query={"_id": uuid})) is not None:
        return existing_team

    raise HTTPException(status_code=404, detail=f"Team {uuid} not found")


@router.delete("/delete-team", response_description="Delete a Team")
async def delete_team(uuid: str):
    delete_result = await mongodb.delete_one(
        data_base=DATABASE, collection=TEAMS_COLLECTION, query={"_id": uuid})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Team {uuid} not found")
