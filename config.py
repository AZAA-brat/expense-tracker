from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
load_dotenv()
import os
from zoneinfo import ZoneInfo

CBU_URL = "https://cbu.uz/en/arkhiv-kursov-valyut/json/{currency}/{date}/"
SAMARKAND = ZoneInfo("Asia/Tashkent")
DB_PATH="tracker.db"
bot_token = os.getenv("BOT_TOKEN")

bot = Bot(token=bot_token)
dp = Dispatcher()
