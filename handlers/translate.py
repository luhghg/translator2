from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from utils.translator import translate_text

router = Router()


class TranslateState(StatesGroup):
    text = State()


@router.message(Command("translate"))
async def cmd_translate(message: types.Message, state: FSMContext):
    await state.set_state(TranslateState.text)
    await message.answer("Введи текст для перевода:")


@router.message(TranslateState.text, F.text)
async def process_translate(message: types.Message, state: FSMContext):
    data = await state.get_data()   # ✅ добавили await
    src = data.get("src", "auto")
    dest = data.get("dest", "en")

    translated = translate_text(message.text, src=src, dest=dest)
    await state.clear()
    await message.answer(f"🔤 Перевод:\n{translated}")
