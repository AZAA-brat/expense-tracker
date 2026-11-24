from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.phrases import ADD_EXPENSE, CATEGORIES, SHOW_REPORT, CHARTS, ADD_CATEGORY

choice_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=CATEGORIES)],
        [KeyboardButton(text=ADD_EXPENSE),
         KeyboardButton(text=ADD_CATEGORY)],
        [KeyboardButton(text=SHOW_REPORT),
         KeyboardButton(text=CHARTS)],

    ],
    resize_keyboard=True
)