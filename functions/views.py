from storage.categories.list import list_categories
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.phrases import NO_CATEGORIES, CATEGORY_LIST
from keyboards.callbacks import CategoryCB

async def show_category(message: Message) -> None:
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
    await message.answer(
        CATEGORY_LIST,
        reply_markup=builder.as_markup(),
    )