from aiogram import Router, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()

# Состояния для FSM
class LanguageState(StatesGroup):
    src = State()   # исходный язык
    dest = State()  # язык перевода

# Хендлер для выбора исходного языка
@router.message(commands=["setlang"])
async def choose_src(message: types.Message, state: FSMContext):
    await state.set_state(LanguageState.src)
    await message.answer("Выбери исходный язык (например, ru, en, ko, ja, la)")

# Обработка ввода исходного языка
@router.message(LanguageState.src)
async def set_src(message: types.Message, state: FSMContext):
    await state.update_data(src=message.text.lower())
    await state.set_state(LanguageState.dest)
    await message.answer("Теперь выбери язык перевода (например, ru, en, ko, ja, la)")
