import logging
from aiogram.filters import Command
from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from states.advert_states import AdvertStates
from services import db_service
from models.advert import Advert
from datetime import datetime
import uuid

router = Router()

@router.message(Command("create_advert"))
async def create_advert(message: types.Message, state: FSMContext):
    await message.answer("Введите город отправления:")
    await state.set_state(AdvertStates.waiting_for_departure_city)

@router.message(AdvertStates.waiting_for_departure_city)
async def set_departure_city(message: types.Message, state: FSMContext):
    await state.update_data(departure_city=message.text)
    await message.answer("Введите город назначения:")
    await state.set_state(AdvertStates.waiting_for_destination_city)

@router.message(AdvertStates.waiting_for_destination_city)
async def set_destination_city(message: types.Message, state: FSMContext):
    await state.update_data(destination_city=message.text)
    await message.answer("Введите дату отправления (в формате ДД.ММ.ГГГГ):")
    await state.set_state(AdvertStates.waiting_for_departure_date)

@router.message(AdvertStates.waiting_for_departure_date)
async def set_departure_date(message: types.Message, state: FSMContext):
    await state.update_data(departure_date=message.text)
    await message.answer("Введите доступный вес (в кг):")
    await state.set_state(AdvertStates.waiting_for_available_weight)

@router.message(AdvertStates.waiting_for_available_weight)
async def set_available_weight(message: types.Message, state: FSMContext):
    await state.update_data(available_weight=float(message.text))
    await message.answer("Введите доступный объем:")
    await state.set_state(AdvertStates.waiting_for_available_volume)

@router.message(AdvertStates.waiting_for_available_volume)
async def set_available_volume(message: types.Message, state: FSMContext):
    await state.update_data(available_volume=float(message.text))
    await message.answer("Введите стоимость перевозки:")
    await state.set_state(AdvertStates.waiting_for_price)

@router.message(AdvertStates.waiting_for_price)
async def set_price(message: types.Message, state: FSMContext):
    await state.update_data(price=float(message.text))
    await message.answer("Введите предпочитаемый способ оплаты (Наличные или Кошелек Telegram):")
    await state.set_state(AdvertStates.waiting_for_payment_method)

@router.message(AdvertStates.waiting_for_payment_method)
async def set_payment_method(message: types.Message, state: FSMContext):
    await state.update_data(payment_method=message.text)
    await message.answer("Введите комментарий (необязательно):")
    await state.set_state(AdvertStates.waiting_for_comment)

@router.message(AdvertStates.waiting_for_comment)
async def set_comment(message: types.Message, state: FSMContext):
    logging.info("Starting to set comment")  # Логирование
    await state.update_data(comment=message.text or "")
    data = await state.get_data()
    logging.info(f"Collected data: {data}")  # Логирование
    advert_data = Advert(
        advert_id=str(uuid.uuid4()),
        courier_id=message.from_user.id,
        departure_city=data['departure_city'],
        destination_city=data['destination_city'],
        departure_date=data['departure_date'],
        available_weight=data['available_weight'],
        available_volume=data['available_volume'],
        price=data['price'],
        payment_method=data['payment_method'],
        comment=data['comment'],
        status="CREATED",
        created_at=datetime.utcnow().isoformat(),
        updated_at=datetime.utcnow().isoformat(),
        responses=[],
        is_deleted=False
    )
    logging.info(f"Advert data to save: {advert_data}")  # Логирование
    db_service.save_advert(advert_data)
    await message.answer(f"Объявление создано: {advert_data}")
    await state.clear()
@router.message(Command("delete_advert"))
async def delete_advert_command(message: types.Message, state: FSMContext):
    await message.answer("Введите ID объявления для удаления:")
    await state.set_state(AdvertStates.waiting_for_advert_id)

@router.message(AdvertStates.waiting_for_advert_id)
async def delete_advert(message: types.Message, state: FSMContext):
    logging.info("Deleting advert")  # Логирование
    advert_id = message.text
    advert = db_service.get_advert_by_id(advert_id)
    logging.info(f"Advert to delete: {advert}")  # Логирование

    if not advert:
        await message.answer("Объявление с таким ID не найдено.")
        await state.clear()
        return

    db_service.delete_advert(advert_id)
    await message.answer(f"Объявление с ID {advert_id} успешно удалено.")
    await state.clear()

@router.message(Command("edit_advert"))
async def edit_advert_command(message: types.Message, state: FSMContext):
    await message.answer("Введите ID объявления для редактирования:")
    await state.set_state(AdvertStates.waiting_for_advert_id_to_edit)

@router.message(AdvertStates.waiting_for_advert_id_to_edit)
async def edit_advert(message: types.Message, state: FSMContext):
    logging.info("Editing advert")  # Логирование
    advert_id = message.text
    advert = db_service.get_advert_by_id(advert_id)
    logging.info(f"Advert to edit: {advert}")  # Логирование

    if not advert:
        await message.answer("Объявление с таким ID не найдено.")
        await state.clear()
        return

    await state.update_data(advert_id=advert_id)
    await message.answer("Введите новое значение для поля или оставьте пустым, чтобы не изменять. Введите новый город отправления:")
    await state.set_state(AdvertStates.waiting_for_new_departure_city)

@router.message(AdvertStates.waiting_for_new_departure_city)
async def set_new_departure_city(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(new_departure_city=message.text)
    await message.answer("Введите новый город назначения:")
    await state.set_state(AdvertStates.waiting_for_new_destination_city)

@router.message(AdvertStates.waiting_for_new_destination_city)
async def set_new_destination_city(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(new_destination_city=message.text)
    await message.answer("Введите новую дату отправления (в формате ДД.ММ.ГГГГ):")
    await state.set_state(AdvertStates.waiting_for_new_departure_date)

@router.message(AdvertStates.waiting_for_new_departure_date)
async def set_new_departure_date(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(new_departure_date=message.text)
    await message.answer("Введите новый доступный вес (в кг):")
    await state.set_state(AdvertStates.waiting_for_new_available_weight)

@router.message(AdvertStates.waiting_for_new_available_weight)
async def set_new_available_weight(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(new_available_weight=message.text)
    await message.answer("Введите новый доступный объем:")
    await state.set_state(AdvertStates.waiting_for_new_available_volume)

@router.message(AdvertStates.waiting_for_new_available_volume)
async def set_new_available_volume(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(new_available_volume=message.text)
    await message.answer("Введите новую стоимость перевозки:")
    await state.set_state(AdvertStates.waiting_for_new_price)

@router.message(AdvertStates.waiting_for_new_price)
async def set_new_price(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(new_price=message.text)
    await message.answer("Введите новый предпочитаемый способ оплаты (Наличные или Кошелек Telegram):")
    await state.set_state(AdvertStates.waiting_for_new_payment_method)

@router.message(AdvertStates.waiting_for_new_payment_method)
async def set_new_payment_method(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(new_payment_method=message.text)
    await message.answer("Введите новый комментарий (необязательно):")
    await state.set_state(AdvertStates.waiting_for_new_comment)

@router.message(AdvertStates.waiting_for_new_comment)
async def set_new_comment(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(new_comment=message.text)
    data = await state.get_data()
    logging.info(f"Data to update advert: {data}")  # Логирование
    advert = db_service.get_advert_by_id(data['advert_id'])
    
    if 'new_departure_city' in data:
        advert.departure_city = data['new_departure_city']
    if 'new_destination_city' in data:
        advert.destination_city = data['new_destination_city']
    if 'new_departure_date' in data:
        advert.departure_date = data['new_departure_date']
    if 'new_available_weight' in data:
        advert.available_weight = float(data['new_available_weight'])
    if 'new_available_volume' in data:
        advert.available_volume = float(data['new_available_volume'])
    if 'new_price' in data:
        advert.price = float(data['new_price'])
    if 'new_payment_method' in data:
        advert.payment_method = data['new_payment_method']
    if 'new_comment' in data:
        advert.comment = data['new_comment']

    advert.updated_at = datetime.utcnow().isoformat()
    db_service.update_advert(advert)
    
    await message.answer(f"Объявление с ID {advert.advert_id} успешно обновлено.")
    await state.clear()