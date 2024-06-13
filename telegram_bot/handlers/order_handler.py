from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("create_order"))
async def create_order(message: Message):
    await message.answer("Создание заказа.")

@router.message(Command("edit_order"))
async def edit_order(message: Message):
    await message.answer("Редактирование заказа.")

@router.message(Command("delete_order"))
async def delete_order(message: Message):
    await message.answer("Удаление заказа.")