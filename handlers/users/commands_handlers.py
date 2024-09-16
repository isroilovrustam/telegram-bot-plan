from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command('til'))
async def handle_til(message: types.Message):
    await message.answer(f"Til o'zgardi!")


# Ikkinchi usul
# @dp.message_handler(commands='til')
# async def handle_til(message: types.Message):
#     await message.answer(f"Til o'zgardi!")
