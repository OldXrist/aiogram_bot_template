from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="ℹ️ About me")],
            [KeyboardButton(text="💬 Support"), KeyboardButton(text="🔧 Settings")]
        ],
        resize_keyboard=True
    )
