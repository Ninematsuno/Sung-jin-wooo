from pyrogram import filters , Client
from nksama import bot
from pymongo import MongoClient as client
from nksama.db import MONGO_URL as url

users_db = client(url)['users']['user']

@bot.on_message(filters.command("start"))
def update_stats(_,message):
  users = users_db.find()
  mfs = []
  for x in users['user_id']:
    mfs.append(x)
  if message.from_user.id not in mfs:
    user = {"type": "user" , "user_id":message.from_user.id}
    users_db.insert_one(user)
    
    
    
    
@bot.on_message(filters.command("stats"))
def stats(_,message):
  users = users_db.find()
  mfs = []
  for x in users['user_id']:
    mfs.append(x)
    
  total = len(mfs)
  
  message.reply_text(f"Total Users: {total}")
  


