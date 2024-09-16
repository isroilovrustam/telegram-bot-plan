from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.message_handler(Text(contains="assalom", ignore_case=True))
@dp.message_handler(Text(equals="assalom alaykum", ignore_case=True))
async def assalom(message: types.Message):
    await message.answer("Vaalaykum assalom")


@dp.message_handler(Text(contains="ahmoq", ignore_case=True))
async def assalom(message: types.Message):
    await message.answer("O'zing ahmoq")
