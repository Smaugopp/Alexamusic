from src.database import db

usersdb = db.users

async def get_served_users() -> list:
    chats = await usersdb.find({"user_id": {"$gt": 0}}).to_list(length=None)
    return [chat["user_id"] for chat in chats]

async def is_served_user(chat_id: int) -> bool:
    chat = await usersdb.find_one({"user_id": chat_id})
    return bool(chat)

async def add_served_user(user_id: int, username: str):
    await usersdb.insert_one(
        {"user_id": user_id, "username": username},
        upsert=True
    )

async def remove_served_user(chat_id: int):
    await usersdb.delete_one({"user_id": chat_id})

async def get_user_coins(user_id: int) -> int:
    user = await usersdb.find_one({"user_id": user_id})
    if user:
        return user.get("coins", 0)
    else:
        # If user does not exist, return 0 coins
        return 0

async def update_user_coins(user_id: int, coins: int):
    await usersdb.update_one(
        {"user_id": user_id},
        {"$set": {"coins": coins}},
        upsert=True
    )

async def add_user_coins(user_id: int, coins_to_add: int):
    current_coins = await get_user_coins(user_id)
    new_coins = current_coins + coins_to_add
    await update_user_coins(user_id, new_coins)

async def deduct_user_coins(user_id: int, coins_to_deduct: int):
    current_coins = await get_user_coins(user_id)
    new_coins = max(0, current_coins - coins_to_deduct)
    await update_user_coins(user_id, new_coins)
