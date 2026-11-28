from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import types, F, Router
from functions.views.for_expenses import show_category_for_expenses
from keyboards.callbacks import CategoryCB
from states import ExpenseState
from utils.phrases import ADD_EXPENSE, ASK_EXPENSE, AMOUNT_EXPENSE

router = Router()

@router.message(F.text == ADD_EXPENSE)
async def category_handler(message: types.Message, state: FSMContext):
    await state.set_state(ExpenseState.choosing_category)
    await show_category_for_expenses(message)

@router.callback_query(CategoryCB.filter(), ExpenseState.choosing_category )
async def handle_expense(callback: CallbackQuery, callback_data: CategoryCB, state: FSMContext):
    await state.update_data(category_id=callback_data.category_id)
    await callback.answer()
    await state.set_state(ExpenseState.name)
    await callback.message.answer(ASK_EXPENSE, parse_mode = "HTML")

@router.message(ExpenseState.amount)
async def handle_amount(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ExpenseState.amount)
    await message.answer(AMOUNT_EXPENSE, parse_mode="HTML")
    data = await state.get_data()
    await message.answer(f"Category you choose: {data['category_id']}"
                            f"The amount spent on it: {data['name']}"
                            f"Name of your expense: {data['amount']}")