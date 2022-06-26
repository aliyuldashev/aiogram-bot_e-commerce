import asyncpg
from aiogram import types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu
import logging
from keyboards.inline import menu_keyboards
from utils.db_api.db_commands import Database as users
from aiogram import Dispatcher
from loader import dp, db, bot
from data.config import ADMINS
from states.main_state import MAIN
from keyboards.inline import menu_keyboards
@dp.callback_query_handler(menu_keyboards.buyurtma_call.filter(),state='*')
async def buyurtma_def(msg:types.CallbackQuery,state:FSMContext,callback_data: dict):
    await bot.send_message(msg.message.chat.id,'ism va familiyangizni kriting')
@dp.callback_query_handler(menu_keyboards.call_call.filter(),state='*')
async def third_call_get(msg:types.CallbackQuery,state:FSMContext,callback_data: dict):
    product = await state.get_data()
    name_call = callback_data.get('name')
    products = await db.selcting_product()
    ishora =  callback_data.get('i')
    text = ''
    mark_up = InlineKeyboardMarkup(row_width=3)
    once = 0
    for dat in products:
        try:
            buyurtma = []
            product1 = product[f"{dat['productname']}"]
            name = dat['productname']
            second = dat['second_tag_id']
            second = await db.selecting_second_tag(second_id=second)
            own_price = dat['price']
            obsh = product1['obn']
            nechta = int(eval(f"{obsh} / {own_price}"))
            if ishora == '-'  and once ==0 and name_call==name:
                obsh = product1['obn']
                nechta= int(int(eval(f"{obsh} / {own_price}")) -1 )
                obsh = int(obsh) - int(own_price)
                if nechta <= 0:
                    continue
                await state.update_data({
                    f'{dat["productname"]}': {'obn': obsh}
                })
                once += 1
            elif ishora == '+' and once ==0 and name_call==name:
                obsh = product1['obn']
                nechta= int(int(eval(f"{obsh} / {own_price}")) +1 )
                obsh = int(obsh) + int(own_price)
                await state.update_data({
                    f'{dat["productname"]}': {'obn': obsh}
                })
                once += 1
            if second[0][0] != 1:
                text += f'\n({second[0][1]}) - {name} dan {nechta} ta \n{nechta} * {own_price} = {obsh} SO`M'
            else:
                text += f'\n{name} dan {nechta} ta \n{nechta} * {own_price} = {obsh} SO`M'
            mark_up.add(
                InlineKeyboardButton(text="-", callback_data=f'cal:{name}:{obsh}:{own_price}:-'),
                InlineKeyboardButton(text=f'{name}', callback_data=f'none'),
                InlineKeyboardButton(text="+", callback_data=f'cal:{name}:{obsh}:{own_price}:+')
            )
            buyurtma.append(name)
        except Exception as ex:
            pass
    mark_up.add(InlineKeyboardButton(text='buyurtma berish'), callback_data=f"btm:{buyurtma}")
    await msg.message.edit_text(text)
    await msg.message.edit_reply_markup(mark_up)
@dp.callback_query_handler(menu_keyboards.savat_cal.filter(),state='*')
async def third_call_get(msg:types.CallbackQuery,state:FSMContext,callback_data: dict):
    product = await state.get_data()
    products = await db.selcting_product()
    text = ''
    mark_up = InlineKeyboardMarkup(row_width=3)
    for dat in products:
        try:
            product1 = product[f"{dat['productname']}"]
            obsh = product1['obn']
            name = dat['productname']
            second = dat['second_tag_id']
            second = await db.selecting_second_tag(second_id=second)
            own_price = (dat['price'])
            nechta= int(eval(f"{obsh} / {own_price}"))
            if second[0][0] != 1:
                text += f'\n({second[0][1]}) - {name} dan {nechta} ta \n{nechta} * {own_price} = {obsh} SO`M'
            else:
                text += f'\n{name} dan {nechta} ta \n{nechta} * {own_price} = {obsh} SO`M'
            mark_up.add(
                InlineKeyboardButton(text="-", callback_data=f'cal:{name}:{obsh}:{own_price}:-'),
                InlineKeyboardButton(text=f'{name}', callback_data=f'None'),
                InlineKeyboardButton(text="+", callback_data=f'cal:{name}:{obsh}:{own_price}:+')
            )
        except Exception as ex:
            print(ex)
    await bot.send_message(msg.message.chat.id,text=text,reply_markup=mark_up)
@dp.callback_query_handler(menu_keyboards.raqam_call.filter(),state='*')
async def third_call_get(msg:types.CallbackQuery,state:FSMContext,callback_data: dict):
    raqam = callback_data.get('ra')
    name = callback_data.get('name')
    first = callback_data.get('first_id')
    second = callback_data.get('second_id')
    esra = callback_data.get('esra')
    number = esra + raqam
    data = await db.four_third_tegs(first_tags=first,second_tags=second,name=name)
    if raqam == 't':
        try:
            number = esra[:-1]
        except:
            pass
    elif esra == '0':
        number = raqam

    else:
        number = esra + raqam
    if raqam == 's':
        mark_up =await menu_keyboards.first_in_get()

        price = data[0]["price"]
        obn = price * int(number[:-1])
        await state.update_data({
            f'{data[0]["productname"]}': {'obn':obn}
        })
    else:
        mark_up = await menu_keyboards.fourth_in_get(first_tag_id=first,second_tag_id=second,name=name,number=number)
    await msg.message.edit_reply_markup(mark_up)
@dp.callback_query_handler(menu_keyboards.cancel_call.filter(), state='*')
async def third_call_get(msg:types.CallbackQuery,state:FSMContext,callback_data: dict):
    name = callback_data.get('name')
    place = callback_data.get('pl')
    first = callback_data.get('first')
    second = callback_data.get('second')
    if place == '2':
        mark_up= await menu_keyboards.first_in_get()
    elif place == '3':
        mark_up = await menu_keyboards.second_in_get(first=first,id=first)
    elif place == '4':
        await msg.answer(cache_time=1)
        mark_up = await menu_keyboards.third_in_get(first=first,second=second)
    await msg.message.edit_reply_markup(mark_up)
@dp.callback_query_handler(menu_keyboards.third_call.filter(), state='*')
async def third_call_get(msg:types.CallbackQuery,state:FSMContext,callback_data: dict):
    first = callback_data.get('first')
    second = callback_data.get('second')
    name = callback_data.get('name')
    mark_up = await menu_keyboards.fourth_in_get(first_tag_id=first,second_tag_id=second,name=name, number=0)
    await msg.message.edit_reply_markup(mark_up)
    #await msg.message.edit_reply_markup(mark_up)
@dp.callback_query_handler(menu_keyboards.second_call.filter(), state='*')
async def second_call_get(msg:types.CallbackQuery,state:FSMContext,callback_data: dict):
    first = callback_data.get('first')
    second = callback_data.get('second')
    mark_up = await menu_keyboards.third_in_get(first=first,second=second)
    await msg.message.edit_reply_markup(mark_up)
@dp.callback_query_handler(menu_keyboards.first_call.filter(), state='*')
async def fisr_call_get(msg:types.CallbackQuery,state:FSMContext,callback_data: dict):
    data =callback_data.get('name')
    id = callback_data.get('id')
    mark_up = await menu_keyboards.second_in_get(first=data,id=id)
    await msg.message.edit_reply_markup(mark_up)
@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    mark_up =await menu_keyboards.first_in_get()
    # if await db.get_users(telegram_id=message.from_user.id):
    await message.answer(f"SIZ BOTNI QAYTA ISHGA TUSHURDINGIZ",reply_markup=mark_up)
    # else:
    #await message.answer(f"Assalomu alaykum {message.from_user.first_name} foydalanuvchi botga hush kelibsiz botdan foydalanish uchun parolni jo`nating")
@dp.message_handler(state = MAIN.parol)
async def send_link(message:types.Message, state: FSMContext):
     try:
         if message.text == 'a':
             user = await db.add_user(
                  telegram_id=message.from_user.id,
                  full_name=message.from_user.full_name,
                  username=message.from_user.username,
             )
             user = await db.select_user(telegram_id=message.from_user.id)
             await message.answer(
                  " Parol to`gri Xush kelibsiz! Do'konimizdagi mahsulotlarni ko'rish uchun quyidagi Menu tugmasini bosing",
                 reply_markup=menu,
             )
             for admin in ADMINS:
                 try:
                     await dp.bot.send_message(admin, f"{message.from_user.full_name} Botga yangi Agent qo`shil")

                 except Exception as err:
                    logging.exception(err)
         else:
             await message.answer(
                 "Parol xato parolni qaytadan jo`nating",
             )
             await MAIN.parol.set()

     except asyncpg.exceptions.UniqueViolationError:
        await message.answer('TIZIMDA XATOLIK YUZBERDI ILTIMOS /start ni bosing')
        await state.finish()




