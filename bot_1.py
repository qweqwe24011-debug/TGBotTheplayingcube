from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from aiogram.types import Message
from royns import router
load_dotenv()
load_dotenv(r"C:\Users\pownkd\Documents\прогромирование\тг\bot_token.env")
TOKEN = getenv('BOT_TOKEN')
dp= Dispatcher()
dp.include_router(router)
async def main():
    bot = Bot(token=TOKEN)
    print("бот запущен")
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())