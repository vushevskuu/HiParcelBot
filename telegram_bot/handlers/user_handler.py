from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    # Пример приветственного сообщения с описанием команд
    welcome_text = (
        "Добро пожаловать! Вот доступные команды:\n"
        "/create_advert - Создать объявление\n"
        "/edit_advert - Редактировать объявление\n"
        "/delete_advert - Удалить объявление\n"
        "/create_order - Создать заказ\n"
        "/edit_order - Редактировать заказ\n"
        "/delete_order - Удалить заказ"
    )
    await message.answer(welcome_text)