from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


@dp.message_handler(filters.Command('chang_photo'), filters.AdminFilter())
@dp.message_handler(commands="ban_user", is_chat_admin=True)
async def ban_user(message: types.Message):
    await message.answer("Rasmni almashtiramizmi?")
