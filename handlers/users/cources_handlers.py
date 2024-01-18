from aiogram import types
from keyboards.default.start_keyboard import cources_keyboard, start_keyboards
from loader import dp
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.cources_keyboard import python_keyboard


@dp.message_handler(text="Kurslar")
async def cources_handler(message: types.Message):
    await message.answer("Kyrlardan birini tanlang: ", reply_markup=cources_keyboard)


@dp.message_handler(text="Python")
async def cources_handler(message: types.Message):
    await message.answer("Darslar: ", reply_markup=python_keyboard)

@dp.message_handler(text="#1-dars")
async def cources_handler(message: types.Message):
    await message.answer("Darsni ko'rishingiz mumkin: ", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Boshiga")
async def cources_handler(message: types.Message):
    await message.answer("Tugmalardan birini bosing: ", reply_markup=start_keyboards)

@dp.message_handler(text="Ortga")
async def cources_handler(message: types.Message):
    await message.answer("Tugmalardan birini bosing: ", reply_markup=cources_keyboard)