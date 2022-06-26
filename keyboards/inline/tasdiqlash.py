from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btasdiq= InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Tasdiqlash", callback_data="tasdiq"),
        InlineKeyboardButton(text="Qayta kiritish", callback_data="bekor"),
        InlineKeyboardButton(text=" bosh menyu", callback_data="cancel"),
    ],
])