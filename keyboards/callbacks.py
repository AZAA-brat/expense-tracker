from aiogram.filters.callback_data import CallbackData

class CategoryCB(CallbackData, prefix="category"):
    category_id: int