import logging
from aiogram import BaseMiddleware
from aiogram.types import Update


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data: dict):
        logging.info(f"Received update: {event}")
        return await handler(event, data)
