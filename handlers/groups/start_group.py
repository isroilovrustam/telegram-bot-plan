from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), CommandStart())
async def start_group(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\nGuruhga xush kelibsiz!!!")


@dp.message_handler(IsGroup(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Yordam kerak bo'lsa adminga murojat qiling!\nhttps://t.me/abdumalikovichuz")

    await message.answer("".join(text))
