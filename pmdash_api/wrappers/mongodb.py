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

# https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html visit to see what each operation does.


def get_database(data_base: str):
    return client[data_base]


def get_collection(data_base: str, collection: str):
    dbname = get_database(data_base=data_base)
    collection = dbname[collection]
    return collection


def insert(data_base: str, collection: str, insert_doc: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    collection.insert_one(insert_doc)


def insert_bulk(data_base: str, collection: str, insert_docs: list[dict]):
    collection = get_collection(data_base=data_base, collection=collection)
    collection.insert_many(insert_docs)


def find_one(data_base: str, collection: str, query: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    collection.find_one(query)


def find(data_base: str, collection: str, query: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    collection.find(query)


def count(data_base: str, collection: str, query: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    collection.count_documents(query)


def update_one(data_base: str, collection: str, query: dict, update: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    collection.update_one(query, update)


def update_may(data_base: str, collection: str, query: dict, update: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    collection.update_many(query, update)


def replace_one(data_base: str, collection: str, query: dict, insert_doc: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    collection.replace_one(query, insert_doc)


def delete_one(data_base: str, collection: str, query: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    collection.delete_one(query)


def delete_many(data_base: str, collection: str, query: dict):
    collection = get_collection(data_base=data_base, collection=collection)
    collection.delete_many(query)
