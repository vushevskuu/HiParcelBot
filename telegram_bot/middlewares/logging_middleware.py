import logging
from aiogram import BaseMiddleware
from aiogram.types import Message

class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        logging.info(f"Получено сообщение: {event.text}")
        return await handler(event, data)