from aiogram import types

from keyboards.inline.callback_data import book_callback
from keyboards.inline.cources_inline import books_inline
from loader import dp
import logging


@dp.callback_query_handler(text="books")
async def boock(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kiroblardan birini tanlang: ", reply_markup=books_inline)
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name="python_book"))
async def buying_book(call: types.CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)
