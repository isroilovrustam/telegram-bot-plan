from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("kitob"))
async def send_book(message: types.Message):
    photo_id = "AgACAgIAAxkBAAILQWW4qUDdizwbryg2VJu0otVv2Px_AAK50jEbgY_ISa4hiwxtiySbAQADAgADeAADNAQ"
    photo_url = "https://avatars.githubusercontent.com/u/105547303?v=4"
    photo_file = InputFile(path_or_bytesio="photos/kitob.jpg")
    await message.reply_photo(
        photo_file, caption="Qancha kerak. \n 500000$ kerakmi 😂"
    )
    await message.answer_photo(
        photo_id, caption="Qancha kerak. \n 100000000$ kerakmi 😂"
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo_url,
        caption="Menman 😂",
    )


@dp.message_handler(Command("kurslar"))
async def send_courses(message: types.Message):
    album = types.MediaGroup()
    photo1 = "AgACAgIAAxkBAAILQWW4qUDdizwbryg2VJu0otVv2Px_AAK50jEbgY_ISa4hiwxtiySbAQADAgADeAADNAQ"
    photo2 = "https://avatars.githubusercontent.com/u/105547303?v=4"
    photo3 = "https://avatars.githubusercontent.com/u/105547303?v=4"
    photo4 = InputFile(path_or_bytesio="photos/kitob.jpg")
    video1 = "BAACAgIAAxkBAAILWGW4rhnFMn0D4TgaPDNyRD0yGONOAALJVQACgY_ISSuPIPycSpzJNAQ"
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)
    album.attach_video(video=video1, caption="Bizning online kurslarimiz")
    await message.reply_media_group(media=album)
