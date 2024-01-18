from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar"),
            KeyboardButton(text="Ma'lumot"),
        ],
        [
            KeyboardButton(text="Aloqa", request_contact=True),
        ],
    ],
    resize_keyboard=True
)


cources_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="Java"),
            KeyboardButton(text="Frontend"),
        ],
        [
            KeyboardButton(text=".Net"),
            KeyboardButton(text="C++"),
        ],
        [
            KeyboardButton(text="Boshiga")
        ],
    ],
    resize_keyboard=True
)