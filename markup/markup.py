from settings import config
from telebot.types import KeyboardButton
from data_base.dbalchemy import DBManager

class Keyboards:

    def __init__(self):
        self.markup = None
        self.DB = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        return KeyboardButton(config.KEYBOARD[name])
