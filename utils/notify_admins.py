import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    try:
        for admin in ADMINS:

            await dp.bot.send_message(admin, "Bot ishga tushdi")

    except:
        pass