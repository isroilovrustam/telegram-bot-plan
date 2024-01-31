from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from keyboards.inline.buy_book import book_keys
from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("kitob"))
async def send_book(message: types.Message):
    photo_id = "AgACAgIAAxkBAAILb2W5_8Z-GrYBNFmIFNXcl4qH_ffjAALy0TEbU1XRSaA2iZN5OUqRAQADAgADeQADNAQ"
    msg = "<b>Pythonda Dasturlash Asoslari</b> kitobi.\n"
    msg += "Narxi: 50000 so'm\n\n"
    msg += "<b>Kitob quyidagi do'konlarda sotiladi:</b>\n👉Akademnashr\n👉Hilol nashr\n👉Azon kitoblar\n👉Kitoblar dunyosi"
    await message.reply_photo(photo_id, caption=msg, reply_markup=book_keys)


@dp.message_handler(Command("kurslar"))
async def send_courses(message: types.Message):
    album = types.MediaGroup()
    photo1 = "AgACAgIAAxkBAAILQWW4qUDdizwbryg2VJu0otVv2Px_AAK50jEbgY_ISa4hiwxtiySbAQADAgADeAADNAQ"
    photo2 = "https://i0.wp.com/mohirdev.uz/wp-content/uploads/photo1627374915.jpeg"
    photo3 = "https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png"
    photo4 = InputFile(path_or_bytesio="photos/algoritm.png")
    video1 = "BAACAgUAAxkBAAIHT2ErOXldS7NxbW9mdL4tsI18ZqlvAALdAgACXltZVVoMJafxpb77IAQ"
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)
    album.attach_video(video=video1, caption="Bizning online kurslarimiz")
    await message.reply_media_group(media=album)
