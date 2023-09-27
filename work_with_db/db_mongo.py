import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_HOST = os.environ.get('MONGO_DB_HOST')
MONGO_DB_PORT = os.environ.get('MONGO_DB_PORT')
MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')


MONGO_URL = f"mongodb://{MONGO_DB_HOST}:{MONGO_DB_PORT}/"
client = pymongo.MongoClient(MONGO_URL)

db = client[MONGO_DB_NAME]

collection = db["mycollection"]

def add_data(name, age):
    data = {"name": name, "age": age}
    collection.insert_one(data)

def retrieve_data():
    return list(collection.find())

def update_data(id, name, age):
    collection.update_one({"_id": id}, {"$set": {"name": name, "age": age}})

def delete_data(id):
    collection.delete_one({"_id": id})


client.close()
