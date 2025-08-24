from abc import ABC, abstractmethod

from aiogram.types import InlineKeyboardButton, KeyboardButton


class Button(ABC):
    @abstractmethod
    def __init__(self):
        pass
