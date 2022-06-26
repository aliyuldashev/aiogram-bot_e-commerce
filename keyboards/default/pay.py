from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

paym = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Naqd"),
            KeyboardButton(text="Plastik"),
            KeyboardButton(text="Mudatli tolov"),
        ],
    ],
    resize_keyboard=True,
)
tasd=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash"),
            KeyboardButton(text="Qayta kiritish"),
        ],
    ],
    resize_keyboard=True,
)