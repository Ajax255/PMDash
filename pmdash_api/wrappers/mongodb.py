import json
import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient

# load_dotenv()

USER = os.environ.get('MONGO_ROOT_USERNAME')
PASSWORD = os.environ.get('MONGO_ROOT_PASSWORD')
CLUSTER_NAME = os.environ.get('MONGO_CLUSTER_NAME')

HOST = os.environ.get('MONGO_URL')
PORT = os.environ.get('MONGO_PORT')

print(f'USER:{USER} PASSWORD:{PASSWORD} CLUSTER_NAME:{CLUSTER_NAME} HOST:{HOST} PORT:{PORT}')

CONNECTION_STRING = f"mongodb://{USER}:{PASSWORD}@{HOST}:{PORT}"

print(f' CONNECTION_STRING:{CONNECTION_STRING}')

client = MongoClient(CONNECTION_STRING)


def get_database(data_base: str):
    return client[data_base]


def create_collection(data_base: str, new_collection: str):
    dbname = get_database(data_base=data_base)
    collection = dbname[new_collection]
    return collection


def insert(data_base: str, new_collection: str, insert_doc: str):
    print(CONNECTION_STRING)
    collection = create_collection(
        data_base=data_base, new_collection=new_collection)
    collection.insert_one(insert_doc)


def insert_bulk(data_base: str, new_collection: str, insert_docs: list[str]):
    collection = create_collection(
        data_base=data_base, new_collection=new_collection)
    collection.insert_many(insert_docs)


def print_connection():
    print(CONNECTION_STRING)
