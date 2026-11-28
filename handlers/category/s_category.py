from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from utils.phrases import ADD_CATEGORY, CATEGORY_FROM_USER, CATEGORY_NAME_EMPTY, CATEGORY_ALREADY_EXISTS, CATEGORY_CREATED
from states import CategoryState
from storage.categories.add import add_category
router = Router()

@router.message(F.text == ADD_CATEGORY)
async def create_category(message: types.Message, state: FSMContext):
    await state.set_state(CategoryState.category)
    await message.answer(CATEGORY_FROM_USER, parse_mode="HTML")

@router.message(CategoryState.category, F.text)
async def process_category_name(message: types.Message, state: FSMContext):
    category_name = message.text.strip()

    if not category_name:
        await message.answer(CATEGORY_NAME_EMPTY)
        return

    category_id = add_category(category_name)

    if category_id is None:
        await message.answer(CATEGORY_ALREADY_EXISTS)
        return

    await state.clear()
    await message.answer(CATEGORY_CREATED.format(name=category_name))




