from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import asyncio
import logging

from .handlers import router
from .database.models import async_main

async def main():
    logging.basicConfig(level=logging.INFO)

    await async_main()

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())