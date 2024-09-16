from aiogram import types
from loader import dp
from aiogram.dispatcher import filters

SUPPERUSER = [43532134, 3454323]
BLACKLIST = [43532134, 213453456]


# @dp.message_handler(filters.IDFilter(chat_id=SUPPERUSER))
@dp.message_handler(chat_id=SUPPERUSER, text='secret')
async def secret_handler(message: types.Message):
    await message.answer("Xush kelibsiz super user!!!")
