from aiogram import Router, types

router = Router()

@router.message(commands=["start"])
async def start_message(message: types.Message):
    await message.answer(
        "Привет! Я бот-переводчик.\n"
        "Сначала выбери язык исходного текста через команду /setlang."
    )
