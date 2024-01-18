from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import ContentType, Message

from loader import dp
from pathlib import Path

# kelgan hujjatlar (rasm/video/audio...) downloads/categories papkasiga tushadi
download_path = Path().joinpath("downloads", "categories")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(content_types=ContentType.PHOTO)
# @dp.message_handler(content_types="photo")
async def photo_handler(message: Message):
    await message.answer("Bu qanday rasm?")


@dp.message_handler(content_types=ContentType.DOCUMENT)
# @dp.message_handler(content_types='document')
async def doc_handler(message: Message):
    await message.document.download(destination=download_path)
    doc_id = message.document.file_id
    await message.reply("Siz hujjat yubordingiz!\n"
                        f"file_id = {doc_id}")


# @dp.message_handler(content_types=ContentType.VIDEO)
@dp.message_handler(content_types='video')
async def video_handler(message: Message):
    await message.video.download(destination=download_path)
    await message.reply("Video qabul qilindi\n"
                        f"file_id = {message.video.file_id}")


@dp.message_handler(content_types=ContentType.VOICE)
async def voice_handler(message: Message):
    await message.voice.download(destination=download_path)
    await message.reply("Yaxshi eshitmadim? ")
