from aiogram import Router, types
from aiogram.filters import Command

from fitlers.admin import IsAdminFilter
from keyboards.inline import example_inline_keyboard
from keyboards.reply import main_menu
from config import ADMINS

router = Router()


@router.message(Command("start"), IsAdminFilter(ADMINS))
async def start_handler_authorized(message: types.Message):
    await message.answer(
        "Hi! I'm your Telegram-bot. How can I help?",
        reply_markup=main_menu()
    )


@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Sorry, you are not authorized to use this bot!",
        reply_markup=main_menu()
    )


@router.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("Example help command", reply_markup=example_inline_keyboard())
