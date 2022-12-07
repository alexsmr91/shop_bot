import os
from emoji import emojize

TOKEN = '5252842398:AAEXW9FMazQX_xwtWJiMVo4Spu-ghF2GeC8'
NAME_DB = 'products.sqlite'
VERSION = '0.0.1'
AUTHOR = 'User'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

KEYBOARD ={
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙ Настройки'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('⬅'),
    'NEXT_STEP': emojize('➡'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOWN': emojize('⬇'),
    'UP': emojize('⬆'),
    'AMOUNT_PRODUCTS': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'APPLY': emojize('✅ Оформить заказ'),
    'COPY': emojize('©')
}

CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3
}

COMMANDS = {
    'START': "start",
    'HELP': "help"
}
