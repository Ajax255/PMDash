from fastapi import APIRouter
from dotenv import load_dotenv, find_dotenv

import os
import models.team as team
from models.member import Memeber
import wrappers.mongodb as mongodb

# Used to load .env for local envion. (Dev Environments)
load_dotenv(find_dotenv())

DATABASE = os.environ.get('MONGO_DATABASE')
MEMBERS_COLLECTION = os.environ.get('MONGO_MEMBERS_COLLECTION')
TEAMS_COLLECTION = os.environ.get('MONGO_TEAMS_COLLECTION')

router = APIRouter(prefix='/pmdash', tags=['PMDash'])

# member endpoints


@router.post('/create-member')
async def create_member(member: Memeber):
    print('create', member)
    return mongodb.insert(data_base=DATABASE, collection=MEMBERS_COLLECTION)


@router.get('/search-members')
async def search_members(search: str):
    print('search', search)
    return mongodb.find_one(data_base=DATABASE, collection=MEMBERS_COLLECTION)


@router.get('/search-all-members')
async def search_all_members():
    print('ran members search')
    return mongodb.find(data_base=DATABASE, collection=MEMBERS_COLLECTION,
                        query={"author": "Mike"})


@router.patch('/update-member')
async def update_member(uuid: str, patch: dict):
    print('update', uuid)
    print('patch', patch)
    return mongodb.update_one(data_base=DATABASE, collection=MEMBERS_COLLECTION)


@router.delete('/delete-member')
async def delete_member(uuid: str):
    print('delete', uuid)
    return mongodb.delete_one(data_base=DATABASE, collection=MEMBERS_COLLECTION)


# team endpoints
@router.post('/create-team')
async def create_team(team: team.Team):
    print('create', team)
    return mongodb.insert(data_base=DATABASE, collection=TEAMS_COLLECTION)


@router.get('/search-teams')
async def search_teams(search: str):
    print('search', search)
    return mongodb.find_one(data_base=DATABASE, collection=TEAMS_COLLECTION)


@router.get('/search-all-teams')
async def search_all_teams():
    print('ran teams search')
    return mongodb.find(data_base=DATABASE, collection=TEAMS_COLLECTION,
                        query={"author": "Mike"})


@router.patch('/update-team')
async def update_team(uuid: str, patch: dict):
    print('update', uuid)
    print('patch', patch)
    return mongodb.update_one(data_base=DATABASE, collection=TEAMS_COLLECTION)


@router.delete('/delete-team')
async def delete_team(uuid: str):
    print('delete', uuid)
    return mongodb.delete_one(data_base=DATABASE, collection=TEAMS_COLLECTION)
