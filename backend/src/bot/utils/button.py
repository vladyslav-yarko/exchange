from abc import ABC, abstractmethod

from aiogram.types import InlineKeyboardButton, KeyboardButton


class Button(ABC):
    @abstractmethod
    def __init__(self):
        pass


class CallbackButton(Button):
    def __init__(self, text: str, callback: str):
        self.text = text
        self.callback = callback
        self.button = InlineKeyboardButton(text=self.text, callback_data=self.callback)
