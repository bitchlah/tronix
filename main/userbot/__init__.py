from .client import app
from pyrogram import Client as Bot
from config import API_ID, API_HASH, BOT_TOKEN, SESSION

client = Bot(STRING_SESSION, API_ID, API_HASH, plugins=dict(root="main.userbot.modules"))
