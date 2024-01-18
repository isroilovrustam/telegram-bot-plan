from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


python_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#1-dars"),
            KeyboardButton(text="#2-dars"),
            KeyboardButton(text="#3-dars"),
        ],
        [
            KeyboardButton(text="#4-dars"),
            KeyboardButton(text="#5-dars"),
            KeyboardButton(text="#6-dars"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),
        ],
    ],
    resize_keyboard=True
)