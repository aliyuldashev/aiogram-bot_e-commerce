from aiogram.dispatcher.filters.state import StatesGroup, State


class BuyurtmaData(StatesGroup):
    zakaz_name = State() # zakaz ismi
    m_soni = State()  # Soni
    karzina = State()
    m_name = State()  # Mijoz nomi
    m_tel = State()  # Tel raqami
    m_man = State()  # Manzili
    t_turi=State() #To`lov turi
    b_tasdiq=State()
    state_start=State()

