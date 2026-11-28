from aiogram.fsm.state import StatesGroup, State

class CategoryState(StatesGroup):
    category = State()

class ExpenseState(StatesGroup):
    choosing_category = State()
    amount = State()
    name = State()
