import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import TOKEN
from handlers import advert_handler, order_handler, user_handler
from middlewares.logging_middleware import LoggingMiddleware  # исправлен путь импорта

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.message.middleware(LoggingMiddleware())

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать работу"),
        BotCommand(command="/create_advert", description="Создать объявление"),
        BotCommand(command="/edit_advert", description="Редактировать объявление"),
        BotCommand(command="/delete_advert", description="Удалить объявление"),
        BotCommand(command="/create_order", description="Создать заказ"),
        BotCommand(command="/edit_order", description="Редактировать заказ"),
        BotCommand(command="/delete_order", description="Удалить заказ"),
    ]
    await bot.set_my_commands(commands)

async def main():
    dp.include_router(advert_handler.router)
    dp.include_router(order_handler.router)
    dp.include_router(user_handler.router)
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())