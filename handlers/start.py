from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот-переводчик 🌍\n\n"
        "1️⃣ Используй /setlang чтобы выбрать языки\n"
        "2️⃣ Потом введи /translate чтобы перевести текст"
    )
