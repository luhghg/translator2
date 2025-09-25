from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()


class LanguageState(StatesGroup):
    src = State()
    dest = State()


@router.message(Command("setlang"))
async def cmd_setlang(message: types.Message, state: FSMContext):
    await state.set_state(LanguageState.src)
    await message.answer("Введи исходный язык (например: en, ru, ja)")


@router.message(LanguageState.src, F.text)
async def process_src(message: types.Message, state: FSMContext):
    await state.update_data(src=message.text.lower())
    await state.set_state(LanguageState.dest)
    await message.answer("Теперь введи язык перевода (например: en, ru, ja)")


@router.message(LanguageState.dest, F.text)
async def process_dest(message: types.Message, state: FSMContext):
    await state.update_data(dest=message.text.lower())
    data = await state.get_data()
    await state.clear()
    await message.answer(
        f"✅ Языки сохранены!\n"
        f"Исходный: {data['src']}\n"
        f"Перевод: {data['dest']}\n\n"
        f"Теперь напиши /translate и введи текст ✍️"
    )
