import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
from handlers.commands import router as commands_router
from middlewares.logging import LoggingMiddleware
from config import BOT_TOKEN
from database.db import init_database

# Enable logging
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    # Initialize the database
    init_database()

    # Register middlewares
    dp.update.middleware(LoggingMiddleware())

    # Register handlers
    dp.include_routers(commands_router)

    # Set bot commands
    await bot.set_my_commands([
        BotCommand(command="start", description="Start bot"),
        BotCommand(command="help", description="Help"),
    ])

    # Start polling
    logging.info("Bot started successfully 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
