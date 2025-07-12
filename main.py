#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 24038328, #get it from https://my.telegram.org/auth
    api_hash="6c8ee61c6eb685fc7cc41eb0c0ec007b", #get it from https://my.telegram.org/auth
    bot_token="7824850069:AAGkh1wedVrVrEq2CwJgcb6fB_SauaBkHh0", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
