from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from handlers.language import LanguageState
from utils.translator import translate_text

router = Router()

# Обработка ввода целевого языка
@router.message(LanguageState.dest)
async def set_dest(message: types.Message, state: FSMContext):
    await state.update_data(dest=message.text.lower())
    await message.answer("Теперь напиши текст для перевода")
    # Меняем состояние на ожидание текста
    await state.set_state("waiting_text")

# Обработка текста для перевода
@router.message(state="waiting_text")
async def translate_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    src = data.get("src")
    dest = data.get("dest")
    text = message.text

    result = translate_text(text, src=src, dest=dest)
    await message.answer(f"Перевод ({src} -> {dest}):\n{result}")

    await state.clear()  # сброс состояния после перевода
