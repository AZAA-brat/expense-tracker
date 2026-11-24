from dotenv import load_dotenv
load_dotenv()
from config import bot, dp
from logging_config import setup_logger
import logging
import asyncio
from storage.scheme.database import init_db
import handlers.start as start
import handlers.category as category
import handlers.categories as categories
init_db()
setup_logger()
dp.include_routers(start.router, category.router, categories.router)
logger = logging.getLogger(__name__)

async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())