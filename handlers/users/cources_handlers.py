from aiogram import types

from keyboards.inline import callback_data
from keyboards.inline.callback_data import cources_callback
from loader import dp
from keyboards.inline.cources_inline import cource_inline, courses_inline, telegram_inline
import logging


@dp.message_handler(text="🖥️️️️️️ Kurslar")
async def kurslar(message: types.Message):
    await message.answer("Tugmalardan birini tanlang: ", reply_markup=cource_inline)


@dp.callback_query_handler(text="courses")
async def cources(call: types.CallbackQuery):
    # callback_data = call.data
    # logging.info(f"{callback_data=}")
    # logging.info(f"{call.from_user.username}")
    await call.message.delete()
    await call.message.answer("Tanlang: ", reply_markup=courses_inline)
    await call.answer(cache_time=60)


@dp.callback_query_handler(cources_callback.filter(item_name="telegram"))
async def telegram(call: types.CallbackQuery, callback_data: dict):
    await call.message.delete()
    logging.info(f"{callback_data=}")
    await call.message.answer("Siz mukammal telegram bot kursini tanladingiz:", reply_markup=telegram_inline)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancel")
async def cancel(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Tugmalardan birini tanlang: ", reply_markup=cource_inline)
    await call.answer(cache_time=60)


