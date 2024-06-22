import asyncio
from pymongo import MongoClient 
from config import MONGO_DB_URI
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from AnonXMusic import app 

DATABASE = MongoClient(MONGO_DB_URI)
DB = DATABASE["MAIN"]["delenable"]

ADMIN = []

async def group_admins(chat_id):
    async for member in app.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS):
        ADMIN.append(member.user.id)
    return ADMIN

def check_groups_enable(group_id: int):
    check_status = DB.find_one({"group_id": group_id})
    if check_status:
        return True
    return False
    
def add_group_enable(group_id: int):
    check_status = DB.find_one({"group_id": group_id})
    if check_status:
        return None
    return DB.insert_one({"group_id": group_id})
    
def remove_group_enable(group_id: int):
    check_status = DB.find_one({"group_id": group_id})
    if not check_status:
        return None
    return DB.delete_one({"group_id": group_id})
    
@app.on_message(filters.command("editmode"))
async def editfunctions(app, message) -> None:
    group_admin = await group_admins(message.chat.id)
    if message.from_user.id not in group_admin:
        return await message.reply("You are not admin.")
    
    if len(message.command) == 1:
        return await message.reply("Usage: /editmode on/off")
    status = message.command[1]
    if status == "on":
        check_status = DB.find_one({"group_id": message.chat.id})
        if not check_status:
            add_group_enable(message.chat.id)
            return await message.reply("Edit mode turned on!")
        else:
            await message.reply("Edit mode already enabled.")
            return
    elif status == "off":
        check_status = DB.find_one({"group_id": message.chat.id})
        if not check_status:
            return await message.reply("Edit mode already disabled!")
        else:    
            remove_group_enable(message.chat.id)
            await message.reply("Edit mode turned off!")
            return
    else:
        return await message.reply("Invalid syntax: Try /editmode [on/off]")
            
@app.on_edited_message(filters.text)
async def workdelete(app, message) -> None:
    status = DB.find_one({"group_id": message.chat.id})
    if not status:
        return
    else:
        group_admin = await group_admins(message.chat.id)
        if message.from_user.id not in group_admin:
            if message.edit_hide != True:
                await message.reply(f"{message.from_user.mention} Just edited a text, I deleted 🤡")
                asyncio.sleep(3)
                await message.delete(True) 
            return
