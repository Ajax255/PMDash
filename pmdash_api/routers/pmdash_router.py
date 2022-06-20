from fastapi import APIRouter
from models.team import Team
from models.member import Member
from dotenv import load_dotenv, find_dotenv

import os
import wrappers.mongodb as mongodb

# Used to load .env for local envion. (Dev Environments)
load_dotenv(find_dotenv())

DATABASE = os.environ.get('MONGO_DATABASE')
MEMBERS_COLLECTION = os.environ.get('MONGO_MEMBERS_COLLECTION')
TEAMS_COLLECTION = os.environ.get('MONGO_TEAMS_COLLECTION')

router = APIRouter(prefix='/pmdash', tags=['PMDash'])


# member endpoints
@router.post('/create-member')
async def create_member(member: Member):
    print('create', member)
    return mongodb.insert(data_base=DATABASE, collection=MEMBERS_COLLECTION, insert_doc=member.dict())


@router.get('/search-for-member')
async def search_for_one_member(searchTerm: str, fields: list[str]):
    query = {}

    for field in fields:
        query[field] = searchTerm

    print('search', query)
    return mongodb.find_one(data_base=DATABASE, collection=MEMBERS_COLLECTION, query=query)


@router.get('/search-all-members')
async def search_all_members(searchTerm: str, fields: list[str]):
    query = {}

    for field in fields:
        query[field] = searchTerm

    print('search', query)
    return mongodb.find(data_base=DATABASE, collection=MEMBERS_COLLECTION, query=query)


@router.patch('/update-member')
async def update_member(uuid: str, patch: dict):
    query = {'_id': uuid}
    update = {"$set": patch}
    print('update', query)
    print('update', update)
    return mongodb.update_one(data_base=DATABASE, collection=MEMBERS_COLLECTION, query=query, update=update)


@router.delete('/delete-member')
async def delete_member(uuid: str):
    query = {'_id': uuid}
    print('delete', query)
    return mongodb.delete_one(data_base=DATABASE, collection=MEMBERS_COLLECTION, query=query)


# team endpoints
@router.post('/create-team')
async def create_team(team: Team):
    print('create', team)
    return mongodb.insert(data_base=DATABASE, collection=TEAMS_COLLECTION, insert_doc=team.dict())


@router.get('/search-for-team')
async def search_for_one_team(searchTerm: str, fields: list[str]):
    query = {}

    for field in fields:
        query[field] = searchTerm

    print('search', query)
    return mongodb.find_one(data_base=DATABASE, collection=TEAMS_COLLECTION, query=query)


@router.get('/search-all-teams')
async def search_all_teams(searchTerm: str, fields: list[str]):
    query = {}

    for field in fields:
        query[field] = searchTerm

    print('search', query)
    return mongodb.find(data_base=DATABASE, collection=TEAMS_COLLECTION, query=query)


@router.patch('/update-team')
async def update_team(uuid: str, patch: dict):
    query = {'_id': uuid}
    update = {"$set": patch}
    print('update', query)
    print('update', update)
    return mongodb.update_one(data_base=DATABASE, collection=TEAMS_COLLECTION, query=query, update=update)


@router.delete('/delete-team')
async def delete_team(uuid: str):
    query = {'_id': uuid}
    print('delete', query)
    return mongodb.delete_one(data_base=DATABASE, collection=TEAMS_COLLECTION, query=query)
