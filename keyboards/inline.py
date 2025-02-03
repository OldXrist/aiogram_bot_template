from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def example_inline_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🌍 Open link", url="https://example.com")],
            [InlineKeyboardButton(text="📞 Contact", callback_data="contact")]
        ]
    )
