from storage.categories.list import list_categories
from aiogram.types import InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.phrases import CANCEL_BUTTON, NO_CATEGORIES, CATEGORY_CHOICE
from keyboards.callbacks import CategoryCB
from keyboards.inline import CANCEL_EXPENSE

async def show_category_for_expenses(message: Message) -> None:
    categories = list_categories()
    builder = InlineKeyboardBuilder()
    if not categories:
        await message.answer(NO_CATEGORIES)
        return
    for category in categories:
        builder.button(
            text=category["category"],
            callback_data=CategoryCB(category_id=category["id"]).pack()
        )
    builder.adjust(2)
    builder.row(
        InlineKeyboardButton(text=CANCEL_BUTTON, callback_data=CANCEL_EXPENSE)
    )
    await message.answer(
        CATEGORY_CHOICE,
        parse_mode="HTML",
        reply_markup=builder.as_markup(),
    )