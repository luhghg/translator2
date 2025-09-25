import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from dotenv import load_dotenv

from handlers import start, language, translate

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# регистрируем роутеры
dp.include_router(start.router)
dp.include_router(language.router)
dp.include_router(translate.router)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="setlang", description="Выбрать языки"),
        BotCommand(command="translate", description="Перевести текст"),
    ]
    await bot.set_my_commands(commands)


async def main():
    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
