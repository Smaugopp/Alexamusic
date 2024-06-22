from pymongo import MongoClient 
from config import MONGO_DB_URI

DATABASE = MongoClient(MONGO_DB_URI)
WELCOME_DB = DATABASE["MAIN"]["welcome"]

def check_welcome_enable(group_id: int):
    check_status = WELCOME_DB.find_one({"group_id": group_id})
    if check_status:
        return True
    return False
    
def add_welcome_enable(group_id: int):
    check_status = WELCOME_DB.find_one({"group_id": group_id})
    if check_status:
        return None
    return WELCOME_DB.insert_one({"group_id": group_id})
    
def remove_welcome_enable(group_id: int):
    check_status = WELCOME_DB.find_one({"group_id": group_id})
    if not check_status:
        return None
    return WELCOME_DB.delete_one({"group_id": group_id})
