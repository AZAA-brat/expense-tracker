from aiogram import types, Router, F
from utils.phrases import CATEGORIES
from functions.views import show_category

router = Router()
@router.message(F.text == CATEGORIES)
async def create_category(message: types.Message):
    await show_category(message)

