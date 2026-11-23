from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.phrases import ADD_EXPENSE, CATEGORIES, SHOW_REPORT, CHARTS

choice_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=ADD_EXPENSE),
         KeyboardButton(text=CATEGORIES)],
        [KeyboardButton(text=SHOW_REPORT),
         KeyboardButton(text=CHARTS)],
    ],
    resize_keyboard=True,
    is_persistent=True
)