from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
load_dotenv()
import os
DB_PATH="tracker.db"
bot_token = os.getenv("BOT_TOKEN")
bot = Bot(token=bot_token)
dp = Dispatcher()
