from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import cources_callback, book_callback

# 1-usul
cource_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="📚 Kitoblar", callback_data="books"),
        ],
        [
            InlineKeyboardButton(text="🔗 Saytga o'tish", url="https://www.w3schools.com/python"),
        ],
        [
            InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="Zo'r bot ekan"),
        ],
    ])

# 2-usul
# Kurslar uchun inline keyboard

courses_inline = InlineKeyboardMarkup(row_width=1)

python = InlineKeyboardButton(text="🐍 Python Dasturlash Asoslari",
                              callback_data=cources_callback.new(item_name="python"))
courses_inline.insert(python)

django = InlineKeyboardButton(text="🌐 Django Web Dasturlash", callback_data=cources_callback.new(item_name="django"))
courses_inline.insert(django)

telegram = InlineKeyboardButton(text="🤖 Mukammal Telegram bot",
                                callback_data=cources_callback.new(item_name="telegram"))
courses_inline.insert(telegram)

algorithm = InlineKeyboardButton(text="📈 Ma'lumotlar Tuzilmasi va Algoritmlar", callback_data="cource:algorithm")
courses_inline.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
courses_inline.insert(back_button)

# 3-usul

books = {
    "Python. Dasturlash asoslari": "python_book",
    "C++. Dasturlash tili": "cpp_book",
    "Mukammal Dasturlash. JavaScript": "js_book",
}

books_inline = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    books_inline.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
books_inline.insert(back_button)

# Har bir kurs uchun tugma
telegram_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Xarid qilish", url="https://mohirdev.uz/courses/telegram/")
    ]
])
telegram_inline.insert(back_button)

algoritm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/algoritmlar/")
    ]
])
