# from typing import Union
# import datetime
# from aiogram import types
# import asyncpg
# import logging
# from aiogram.types import CallbackQuery, Message ,KeyboardButton
# from keyboards.default.start_keyboard import menu, menu1
# from keyboards.default.pay import tasd, paym
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
# from data.config import ADMINS
# from keyboards.inline.tasdiqlash import btasdiq
# from states.buystate import BuyurtmaData
# from keyboards.inline.menu_keyboards import (
#     menu_cd,
#     # categories_keyboard,
#     # subcategories_keyboard,
#     # items_keyboard,
#     # item_keyboard,
#     buy_item,
#
# )
#
# from loader import dp, db
# from . import menu_handlers
#
# @dp.callback_query_handler(buy_item.filter(),state='*')
# async def nam_item(callback: CallbackQuery,  state: FSMContext, callback_data : dict):
#      item_id = callback_data.get('item_id')
#      item = await db.get_product(item_id)
#      z_nomi=f"{item['productname']}"
#      m_narxi=item['price']
#      await state.update_data(
#           {
#              "zakaznomi": z_nomi,
#              "mnarx": m_narxi,
#          }
#      )
#      text=f'Tanlagan maxsulotingiz: {z_nomi}  \n'
#      text+=f'Maxsulot miqdorini kiriting kg da MISOL UCHUN (78)'
#
#      await callback.message.answer(text=text, reply_markup=menu)
#      await BuyurtmaData.karzina.set()
#
# @dp.message_handler(state=BuyurtmaData.m_soni)
# async def maxsulot_soni(message: types.Message, state: FSMContext):
#     try:
#         if message.text.isdigit():
#             maxs_soni = int(message.text)
#             data = await state.get_data()
#             name = data.get("zakaznomi")
#             narx = data.get("mnarx")
#             agent_nomi = message.from_user.first_name
#             umum_narx=narx*maxs_soni
#             await state.update_data(
#                 {
#                     "maxs_soni": maxs_soni,
#                     'umum_narx':umum_narx,
#                     'agent_nomi':agent_nomi,
#                 }
#             )
#             text=f'Tanlangan maxsulot {name} \n'
#             text+=f'Buyurtma miqdori: {maxs_soni} kg \n'
#             text+=f'Umumiy narxi: {umum_narx}\n'
#             text+=f'Buyurtmachi ismini kiriting'
#             await message.answer(text, reply_markup=menu)
#             # await PersonalData.email.set()
#             await BuyurtmaData.m_name.set()
#         else:
#             await message.answer('''NO`TO`GRI MALUMOT KRITINGIZ
# ILTIMOS MALUMOTNI TEKSHIRIB QAYTADAN KRITING''')
#             await BuyurtmaData.m_soni.set()
#     except:
#         await message.answer('''TIZIMDA XATOLIK YUZBERDI
# ILTIMOS /start TUGMASINI BOSING''')
#         await state.finish()
# @dp.message_handler(state=BuyurtmaData.m_name)
# async def answer_email(message: types.Message, state: FSMContext):
#     try:
#         if not message.text.isdigit() and len(message.text) > 10:
#             mijoz_nomi = message.text
#             await state.update_data(
#                 {"m_nomi": mijoz_nomi}
#             )
#             await message.answer("Mijoz telefonTelefon raqam kiriting", reply_markup=menu)
#
#             await BuyurtmaData.m_tel.set()
#         else:
#             await message.answer("""NO`TO`GRI MALUMOT KRITINGIZ
# ILTIMOS TEKSHIRIB QAYTADAN KRITING""")
#
#             await BuyurtmaData.m_name.set()
#     except:
#         await message.answer('''TIZIMDA XATOLIK YUZBERDI
#         ILTIMOS /start TUGMASINI BOSING''')
#         await state.finish()
# @dp.message_handler(state=BuyurtmaData.m_tel)
# async def answer_phone(message: types.Message, state: FSMContext):
#     try:
#         number = 'qwertyuiopasdfghjkl;zxcvbnm!@#$%^&*()_=}{|":?><'
#         pro = ' '
#         if not pro in message.text and message.text[0] =='+' and len(message.text) >12 and len(message.text) <16 and not str(message.text[1:-1]).isalpha()  :
#             phone = message.text
#             await state.update_data(
#                 {"tel_raqam": phone}
#             )
#             await message.answer("Mijoz manzilini kirting",reply_markup=menu)
#             await BuyurtmaData.m_man.set()
#         else:
#             await message.answer("""NO`TO`GRI MALUMOT KRITINGIZ
#     ILTIMOS TEKSHIRIB QAYTADAN KRITING""")
#
#             await BuyurtmaData.m_tel.set()
#     except:
#         await message.answer('''TIZIMDA XATOLIK YUZBERDI
#             ILTIMOS /start TUGMASINI BOSING''')
#         await state.finish()
# @dp.message_handler(state=BuyurtmaData.m_man)
# async def answer_phone(message: types.Message, state: FSMContext):
#     try:
#         if len(message.text) >15:
#             manzili = message.text
#             await state.update_data(
#                 {"manzil": manzili}
#             )
#             await message.answer("To`lov turini tanlang", reply_markup=paym)
#             await BuyurtmaData.t_turi.set()
#         else:
#             await message.answer("""NO`TO`GRI MALUMOT KRITINGIZ
#     ILTIMOS TEKSHIRIB QAYTADAN KRITING""")
#
#             await BuyurtmaData.m_man.set()
#     except:
#         await message.answer('''TIZIMDA XATOLIK YUZBERDI
#             ILTIMOS /start TUGMASINI BOSING''')
#         await state.finish()
# @dp.message_handler(state=BuyurtmaData.karzina)
# async def answer_phone(message: types.Message, state: FSMContext):
#     try:
#             await BuyurtmaData.next()
#             maxs_soni = int(message.text)
#             data = await state.get_data()
#             name = data.get("zakaznomi")
#             narx = data.get("mnarx")
#             agent_nomi = message.from_user.first_name
#             umum_narx = narx * maxs_soni
#             await state.update_data(
#                 {
#                     "maxs_soni": maxs_soni,
#                     'umum_narx': umum_narx,
#                     'agent_nomi': agent_nomi,
#                 }
#             )
#             data = await state.get_data()
#             zakaznomi = data.get("zakaznomi")
#             m_soni=data.get('maxs_soni')
#             umum_nar=data.get('umum_narx')
#             await state.update_data({
#                 f"zakazlar_{zakaznomi}":{
#                     'kg':f"{m_soni}",
#                     'obn':f'{umum_nar}'
#                 }
#             })
#
#             data = await state.get_data()
#
#             products = await db.selcting_product()
#             for data1 in products:
#                 try:
#                     data2 = data[f"zakazlar_{data1['productname']}"]
#                     await message.answer(f"{data2['kg']}ta {data1['productname']}\n"
#                                          f"{data2['kg']} * {data1['price']} = {data2['obn']}\n"
#                                          ,reply_markup=menu1)
#                 except Exception as ex:
#                     pass
#             await message.answer(f"davom etish uchun bosh menyu tugmasini bosing \n tugatgan bo`lsangiz buyurtmachini ismini kriting")
#     except Exception as ex:
#         pass
#
#
#
#
#
# @dp.message_handler(state=BuyurtmaData.t_turi)
# async def answer_phone(message: types.Message, state: FSMContext):
#     try:
#         if message.text =='Naqd' or message.text =='Plastik' or message.text =='Mudatli tolov':
#             tolov_turi = message.text
#
#             await state.update_data(
#                 {"pay": tolov_turi}
#             )
#             # Ma`lumotlarni qayta o'qiymiz
#             data = await state.get_data()
#             zakaznomi = data.get("zakaznomi")
#             mnarx=data.get('mnarx')
#             m_soni=data.get('maxs_soni')
#             umum_nar=data.get('umum_narx')
#             mij_nomi=data.get('m_nomi')
#             agent=data.get('agent_nomi')
#             telraqam=data.get('tel_raqam')
#             m_manzil=data.get('manzil')
#             t_turi=data.get('pay')
#             data = await state.get_data()
#             products = await db.selcting_product()
#             msg1 = ''
#             obn = 0
#             for data1 in products:
#                 try:
#                     data2 = data[f"zakazlar_{data1['productname']}"]
#                     msg1 += f"{data2['kg']}ta {data1['productname']}\n" \
#                            f"{data2['kg']} * {data1['price']} = {data2['obn']}\n"
#                     obn = eval(f"{obn} +{data2['obn']}")
#                 except Exception as ex:
#                     pass
#             msg = "Quyidai ma`lumotlar qabul qilindi:\n"
#             msg += msg1
#             msg += f'umumiy narx {obn}\n'
#             msg += f'Mijoz ismi:- {mij_nomi}\n'
#             msg += f"Tel raqami: - {telraqam}\n"
#             msg +=f"Manzili:-{m_manzil}\n"
#             msg +=f"To`lov turi:-{t_turi}\n"
#             msg +=f"Agent ismi:-{agent}\n"
#             msg += f"Agent tg id:-{message.from_user.id}\n"
#             await message.answer(msg, reply_markup=btasdiq)
#             await BuyurtmaData.b_tasdiq.set()
#         else:
#             await message.answer("""NO`TO`GRI MALUMOT KRITINGIZ
#     ILTIMOS TEKSHIRIB QAYTADAN KRITING""")
#
#             await BuyurtmaData.t_turi.set()
#     except:
#         await message.answer('''TIZIMDA XATOLIK YUZBERDI
#             ILTIMOS /start TUGMASINI BOSING''')
#         await state.finish()
# @dp.callback_query_handler(text="tasdiq",state=BuyurtmaData.b_tasdiq)
# async def tasdiq_courses(call: CallbackQuery, state:FSMContext):
#     data = await state.get_data()
#     umum_nar = data.get('umum_narx')
#     mij_nomi = data.get('m_nomi')
#     agent = data.get('agent_nomi')
#     telraqam = data.get('tel_raqam')
#     m_manzil = data.get('manzil')
#     t_turi = data.get('pay')
#     bvaqti=datetime.datetime.now()
#     try:
#         data = await state.get_data()
#         products = await db.selcting_product()
#         msg1 = ''
#         obn = 0
#         for data1 in products:
#             try:
#                 data2 = data[f"zakazlar_{data1['productname']}"]
#                 msg1 += f"{data2['kg']}ta {data1['productname']}\n" \
#                         f"{data2['kg']} * {data1['price']} = {data2['obn']}\n"
#                 obn = eval(f"{obn} +{data2['obn']}")
#                 buyurtma = await db.buyurtma_add(
#                     zakaz_name=data1['productname'],
#                     m_price=data1['price'],
#                     m_soni=data['kg'],
#                     s_price=data['obn'],
#                     m_name=mij_nomi,
#                     m_tel=telraqam,
#                     m_man=m_manzil,
#                     m_agent=agent,
#                     m_time=bvaqti,
#                     agent_id=call.message.chat.id,
#                     t_turi=t_turi,
#                 )
#             except Exception as ex:
#                 pass
#     except asyncpg.exceptions.UniqueViolationError:
#         user = await db.select_user(telegram_id=call.message.from_user.id)
#     msg = "Yangi buyurtma qabul qilindi:\n"
#     msg += msg1
#     msg += f'umumiy narx: {obn}\n'
#     msg += f'Mijoz ismi:- {mij_nomi}\n'
#     msg += f"Tel raqami: - {telraqam}\n"
#     msg += f"Manzili:-{m_manzil}\n"
#     msg += f"To`lov turi:-{t_turi}\n"
#     msg += f"Agent ismi:-{agent}"
#     for admin in ADMINS:
#         try:
#             await dp.bot.send_message(admin, msg)
#         except Exception as err:
#             logging.exception(err)
#     text="Buyurtmangiz  mufaqiyatli qabul qilindi tez fursatlarda yetkazib beramiz"
#     await call.message.answer(text=text, reply_markup=menu)
#     await state.finish()
#
#
# @dp.callback_query_handler(text="bekor", state=BuyurtmaData.b_tasdiq)
# async def tasdiq_courses(call: CallbackQuery, state: FSMContext):
#     #     # State dan chiqaramiz
#     #     # 1-variant
#     text = f"Buyurtmani qayta kitishni tanladiz \n"
#     text+= f'Maxsulotni miqdorini qayta jo`nating'
#     await state.finish()
#     await call.message.answer(text=text, reply_markup=menu)
#
# @dp.callback_query_handler(text="cancel", state='*')
# async def tasdiq_courses(call: CallbackQuery, state: FSMContext):
#
#     text = '''SIZ BOSH SAXIFAGA QAYTDINGIZ
# BOSHIDAN BOSHLASH UCHUN bosh menyu TUGMASINI BOSING'''
#     await state.finish()
#     await call.message.answer(text=text, reply_markup=menu)
#     await state.finish()