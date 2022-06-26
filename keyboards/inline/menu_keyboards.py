import logging
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import db

# Turli tugmalar uchun CallbackData-obyektlarni yaratib olamiz
menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "item_id")
buy_item = CallbackData("buy", "item_id")
first_call = CallbackData('fr','name','id')
second_call = CallbackData('sc','name','first','second')
third_call = CallbackData('tr','name','first','second')
cancel_call = CallbackData('cancel','name','first','second','pl')
raqam_call = CallbackData('r','first_id','second_id','name','esra','ra')
savat_cal = CallbackData('savat','number')
call_call = CallbackData('cal','name','obn','own_price','i')
buyurtma_call = CallbackData('btm','buyurtmalar')
# # Quyidagi funksiya yordamida menyudagi har bir element uchun calbback data yaratib olinadi
# # Agar mahsulot kategoriyasi, ost-kategoriyasi va id raqami berilmagan bo'lsa 0 ga teng bo'ladi
# def make_callback_data(level, category="0", subcategory="0", item_id="0"):
#     return menu_cd.new(
#         level=level, category=category, subcategory=subcategory, item_id=item_id
#     )
# # Bizning menu 3 qavat (LEVEL) dan iborat
# # 0 - Kategoriyalar
# # 1 - Ost-kategoriyalar
# # 2 - Mahsulotlar
# # 3 - Yagona mahsulot
#
#
# # Kategoriyalar uchun keyboardyasab olamiz
# async def categories_keyboard():
#     # Eng yuqori 0-qavat ekanini ko'rsatamiz
#     CURRENT_LEVEL = 0
#
#     # Keyboard yaratamiz
#     markup = InlineKeyboardMarkup(row_width=1)
#
#     # Bazadagi barcha kategoriyalarni olamiz
#     categories = await db.get_categories()
#     # Har bir kategoriya uchun quyidagilarni bajaramiz:
#     for category in categories:
#         # Kategoriyaga tegishli mahsulotlar sonini topamiz
#         number_of_items = await db.count_products(category["category_code"])
#
#         # Tugma matnini yasab olamiz
#         button_text = f"{category['category_name']} ({number_of_items} dona)"
#
#         # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
#         callback_data = make_callback_data(
#             level=CURRENT_LEVEL + 1, category=category["category_code"]
#         )
#         otmen = InlineKeyboardButton(text='boshidan',callback_data= 'cancel')
#
#         # Tugmani keyboardga qo'shamiz
#         markup.insert(
#             InlineKeyboardButton(text=button_text, callback_data=callback_data)
#         )
#     markup.insert(otmen)
#     # Keyboardni qaytaramiz
#     return markup
#
#
# # Berilgan kategoriya ostidagi kategoriyalarni qaytaruvchi keyboard
# async def subcategories_keyboard(category):
#     CURRENT_LEVEL = 1
#     markup = InlineKeyboardMarkup(row_width=1)
#
#     # Kategoriya ostidagi kategoriyalarni bazadan olamiz
#     subcategories = await db.get_subcategories(category)
#     for subcategory in subcategories:
#         # Kategoriyada nechta mahsulot borligini tekshiramiz
#         number_of_items = await db.count_products(
#             category_code=category, subcategory_code=subcategory["subcategory_code"]
#         )
#
#         # Tugma matnini yasaymiz
#         button_text = f"{subcategory['subcategory_name']} ({number_of_items} dona)"
#         # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
#         callback_data = make_callback_data(
#             level=CURRENT_LEVEL + 1,
#             category=category,
#             subcategory=subcategory["subcategory_code"],
#         )
#         markup.insert(
#             InlineKeyboardButton(text=button_text, callback_data=callback_data)
#         )
#
#     # Ortga qaytish tugmasini yasaymiz (yuoqri qavatga qaytamiz)
#     markup.row(
#         InlineKeyboardButton(
#             text="⬅️Ortga", callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
#         )
#     )
#     return markup
#
#
# # Ostkategoriyaga tegishli mahsulotlar uchun keyboard yasaymiz
# async def items_keyboard(category, subcategory):
#     CURRENT_LEVEL = 2
#
#     markup = InlineKeyboardMarkup(row_width=1)
#
#     # Ost-kategorioyaga tegishli barcha mahsulotlarni olamiz
#     items = await db.get_products(category, subcategory)
#     for item in items:
#         # Tugma matnini yasaymiz
#         button_text = f"{item['productname']} - {item['price']} so`m"
#         # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
#         callback_data = make_callback_data(
#             level=CURRENT_LEVEL + 1,
#             category=category,
#             subcategory=subcategory,
#             item_id=item["id"],
#         )
#         markup.insert(
#             InlineKeyboardButton(text=button_text, callback_data=callback_data)
#         )
#
#     # Ortga qaytish tugmasi
#     markup.row(
#         InlineKeyboardButton(
#             text="⬅️Ortga",
#             callback_data=make_callback_data(
#                 level=CURRENT_LEVEL - 1, category=category
#             ),
#         )
#     )
#     return markup
#
#
# # Berilgan mahsulot uchun Xarid qilish va Ortga yozuvlarini chiqaruvchi tugma keyboard
# def item_keyboard(category, subcategory, item_id):
#     CURRENT_LEVEL = 3
#     markup = InlineKeyboardMarkup(row_width=1)
#     markup.row(
#         InlineKeyboardButton(
#             text=f"🛒 Xarid qilish", callback_data=buy_item.new(item_id=item_id)
#         )
#     )
#     markup.row(
#         InlineKeyboardButton(
#             text="⬅️Ortga",
#             callback_data=make_callback_data(
#                 level=CURRENT_LEVEL - 1, category=category, subcategory=subcategory
#             ),
#         )
#     )
#     return markup
async def first_in_get():
    mark_up = InlineKeyboardMarkup(row_width=3)
    data = await db.first_catigory_selection()
    for dat in  data:
        Key = InlineKeyboardButton(text=f'{dat["name"]}', callback_data=f'fr:{dat["name"]}:{dat["id"]}')
        mark_up.insert(Key)
    mark_up.add(InlineKeyboardButton(text='SAVAT',callback_data='savat:10'))
    return mark_up
async def second_in_get(first,id):
    mark_up = InlineKeyboardMarkup(row_width=3)
    data = await db.getting_second_tegs(first_tags=id)
    for dat in data:
        second =await db.selecting_second_tag(second_id=dat['second_tag_id'])
        if dat['second_tag_id'] == 1:
            key = InlineKeyboardButton(text=f'{dat["productname"]}', callback_data=f'tr:{dat["productname"]}:{id}:1')
            mark_up.insert(key)
        else:
            key = InlineKeyboardButton(text=f'{second[0]["name"]}',
                                       callback_data=f'sc:{dat["productname"]}:{id}:{dat["second_tag_id"]}')
            mark_up.insert(key)
    mark_up.insert(InlineKeyboardButton(text='orqaga',
                                        callback_data=f'cancel:{dat["productname"]}:{id}:{dat["second_tag_id"]}:2'))
    return mark_up
async def third_in_get(first, second):
    mark_up = InlineKeyboardMarkup(row_width=3)
    data = await db.getting_third_tegs(first_tags=first,second_tags=second)
    for dat in data:
        key = InlineKeyboardButton(text=f'{dat["productname"]}', callback_data=f'tr:{dat["productname"]}:{first}:{second}')
        mark_up.insert(key)
    mark_up.insert(InlineKeyboardButton(text='orqaga',
                                        callback_data=f'cancel:{dat["productname"]}:{first}:{dat["second_tag_id"]}:3'))
    return mark_up
async def fourth_in_get(first_tag_id,second_tag_id,name,number):
    data = await db.four_third_tegs(first_tags=first_tag_id,second_tags=second_tag_id,name=name)
    name = data[0]['productname']
    mark_up = InlineKeyboardMarkup(row_width=3)
    mark_up.insert(
        InlineKeyboardButton(text=f'Tanlangan: {number}', callback_data=f'tanlangan')
    )
    mark_up.add(
        InlineKeyboardButton(text=f'1',
                             callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:1'),
    InlineKeyboardButton(text=f'2',
                         callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:2'),
    InlineKeyboardButton(text=f'3',
                         callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:3')
    )
    mark_up.add(
        InlineKeyboardButton(text=f'4',
                             callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:4'),
        InlineKeyboardButton(text=f'5',
                             callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:5'),
        InlineKeyboardButton(text=f'6',
                             callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:6')
    )
    mark_up.add(
        InlineKeyboardButton(text=f'7',
                             callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:7'),
        InlineKeyboardButton(text=f'8',
                             callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:8'),
        InlineKeyboardButton(text=f'9',
                             callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:9')
    )
    mark_up.add(
        InlineKeyboardButton(text=f'menyu',
                             callback_data=f'cancel:{name}:{first_tag_id}:{second_tag_id}:2'),
        InlineKeyboardButton(text=f'0',
                             callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:0'),
        InlineKeyboardButton(text=f'tozalash',
                             callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:t')
    )
    mark_up.add(InlineKeyboardButton(text='orqaga',
                                     callback_data=f'cancel:{name}:{first_tag_id}:{second_tag_id}:4'),
                InlineKeyboardButton(text='Savatga qo`shish',callback_data=f'r:{first_tag_id}:{second_tag_id}:{name}:{number}:s'))
    return mark_up