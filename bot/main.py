import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from motor import motor_asyncio

import hendlers

load_dotenv()

# Подрубаем mongodb
cluster = motor_asyncio.AsyncIOMotorClient(os.getenv('MONGODB'))
db = cluster.samlpeDB
coll = db.sample_collection


# Бот
async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=os.getenv('TOKEN'), parse_mode='HTML')
    dp = Dispatcher()
    dp.include_routers(
        hendlers.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
