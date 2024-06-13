from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME
from models.advert import Advert

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
adverts_collection = db["adverts"]

def save_advert(advert: Advert):
    adverts_collection.insert_one(advert.dict())

def get_advert_by_id(advert_id: str):
    return adverts_collection.find_one({"advert_id": advert_id})

def delete_advert(advert_id: str):
    adverts_collection.delete_one({"advert_id": advert_id})

def update_advert(advert: Advert):
    adverts_collection.replace_one({"advert_id": advert.advert_id}, advert.dict())