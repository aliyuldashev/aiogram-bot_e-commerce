from typing import Union

from aiogram import types
from aiogram.types import CallbackQuery, Message

# from keyboards.inline.menu_keyboards import (
#     menu_cd,
#     categories_keyboard,
#     subcategories_keyboard,
#     items_keyboard,
#     item_keyboard,
# # )
# from loader import dp, db
# from aiogram.dispatcher import FSMContext
# @dp.message_handler(text="o`chirish", state='*')
# async def show_menu(message: types.Message , state:FSMContext ):
#     # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
#     await message.answer('malumot o`chirildi')
#     await list_categories(message)
#     await state.finish()
# # Bosh menyu uchun
# @dp.message_handler(text="Bosh menyu", state='*')
# async def show_menu(message: types.Message , state:FSMContext ):
#     # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
#     await list_categories(message)
# @dp.message_handler(text="yana", state='*')
# async def show_menu(message: types.Message , state:FSMContext ):
#     # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
#     await list_categories(message)
# @dp.message_handler(text="Xisobot")
# async def show_menu(message: types.Message):
#     await message.answer(f'{message.from_user.first_name} siz uchun hali hisobot tayor bo`lmadi')
#
#
#
# async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
#     try:
#         markup = await categories_keyboard()
#         if markup["inline_keyboard"] == []:
#             await message.answer("""MAXSULOT TAYOR EMAS
# /start TUGMASINI BOSING
# VA OZGINA KUTING""")
#
#         else:
#             if isinstance(message, Message):
#                 await message.answer("Bo'lim tanlang", reply_markup=markup)
#
#             elif isinstance(message, CallbackQuery):
#                 call = message
#                 await call.message.edit_reply_markup(markup)
#     except:
#         await message.answer("""MAXSULOT TAYOR EMAS
# /start TUGMASINI BOSING
# VA OZGINA KUTING""" )
#
#
# # Ost-kategoriyalarni
# async def list_subcategories(callback: CallbackQuery, category, **kwargs):
#     markup = await subcategories_keyboard(category)
#     await callback.message.edit_reply_markup(markup)
# async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
#     markup = await items_keyboard(category, subcategory)
#     await callback.message.edit_text(text="Mahsulot tanlang", reply_markup=markup)
# async def show_item(callback: CallbackQuery, category, subcategory, item_id):
#     markup = item_keyboard(category, subcategory, item_id)
#     item = await db.get_product(item_id)
#     if item["photo"]:
#         text = f"<a href=\"{item['photo']}\">{item['productname']}</a>\n\n"
#     else:
#         text = f"{item['productname']}\n\n"
#     text += f"Narxi: {item['price']} so`m \n{item['description']}"
#     await callback.message.edit_text(text=text, reply_markup=markup)
# @dp.callback_query_handler(menu_cd.filter(), state='*')
# async def navigate(call: CallbackQuery, callback_data: dict):
#     current_level = callback_data.get("level")
#     category = callback_data.get("category")
#     subcategory = callback_data.get("subcategory")
#     item_id = int(callback_data.get("item_id"))
#     levels = {
#         "0": list_categories,  # Kategoriyalarni qaytaramiz
#         "1": list_subcategories,  # Ost-kategoriyalarni qaytaramiz
#         "2": list_items,  # Mahsulotlarni qaytaramiz
#         "3": show_item,  # Mahsulotni ko'rsatamiz
#     }
#     #Foydalanuvchidan
#     current_level_function = levels[current_level]
#     await current_level_function(
#         call, category=category, subcategory=subcategory, item_id=item_id
#     )
#
