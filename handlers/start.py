import html
from aiogram import Router, types
from aiogram.filters import CommandStart
from storage.users.update import update_username
from storage.users.get_or_create import get_or_create_user
from utils.phrases import GREETING, START_ERROR
from keyboards.reply import choice_kb
router = Router()

@router.message(CommandStart())
async def handle_start(message: types.Message):
    from_user = message.from_user
    if from_user is None:
        await message.answer(START_ERROR, parse_mode="HTML")

    user = get_or_create_user(
        telegram_id=from_user.id,
        username=from_user.username,
    )

    if user["username"] != from_user.username:
        update_username(
            telegram_id=from_user.id,
            username=from_user.username,
        )

    display_name = (from_user.username or from_user.first_name or "there")

    await message.answer(
        GREETING.format(name=html.escape(display_name)),parse_mode="HTML", reply_markup=choice_kb)