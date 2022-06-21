import os
import json
from typing import Dict
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

# Used to load .env for local envion. (Dev Environments
load_dotenv(find_dotenv())

USER = os.environ.get('MONGO_ROOT_USERNAME')
PASSWORD = os.environ.get('MONGO_ROOT_PASSWORD')
CLUSTER_NAME = os.environ.get('MONGO_CLUSTER_NAME')

HOST = os.environ.get('MONGO_URL')
PORT = os.environ.get('MONGO_PORT_EXPOSED')

CONNECTION_STRING = f"mongodb://{USER}:{PASSWORD}@{HOST}:{PORT}"

print(f' CONNECTION_STRING:{CONNECTION_STRING}')

client = MongoClient(CONNECTION_STRING)
db = client.college

# https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html visit to see what each operation does.


def get_database(data_base: str):
    return client[data_base]


def get_collection(data_base: str, collection: str):
    dbname = get_database(data_base=data_base)
    collection = dbname[collection]
    return collection


async def insert(data_base: str, collection: str, insert_doc):
    collection = get_collection(data_base=data_base, collection=collection)
    return collection.insert_one(insert_doc)


async def insert_bulk(data_base: str, collection: str, insert_docs: list[dict]):
    collection = get_collection(data_base=data_base, collection=collection)
    return collection.insert_many(insert_docs)


async def find_one(data_base: str, collection: str, query: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    return collection.find_one(query)


async def find(data_base: str, collection: str, query: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    return collection.find(query)


async def count(data_base: str, collection: str, query: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    return collection.count_documents(query)


async def update_one(data_base: str, collection: str, query: dict, update: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    return collection.update_one(query, update)


async def update_may(data_base: str, collection: str, query: dict, update: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    return collection.update_many(query, update)


async def replace_one(data_base: str, collection: str, query: dict, insert_doc: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    return collection.replace_one(query, insert_doc)


async def delete_one(data_base: str, collection: str, query: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    return collection.delete_one(query)


async def delete_many(data_base: str, collection: str, query: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    return collection.delete_many(query)
