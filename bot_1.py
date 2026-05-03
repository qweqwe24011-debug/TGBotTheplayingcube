import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from pathlib import Path
from royns import router
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv("BOT_TOKEN")
print("ENV PATH:", env_path)
if not TOKEN:
    raise ValueError("BOT_TOKEN не найден")
dp = Dispatcher()
dp.include_router(router)
async def main():
    bot = Bot(token=TOKEN)
    print("бот запущен")
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())