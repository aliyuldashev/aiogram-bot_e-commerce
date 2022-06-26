import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        await bot.send_message(
            chat_id=user, text="Yangi maxsulot qoshildi kanaliga obuna bo'ling!"
        )
        await asyncio.sleep(0.05)
