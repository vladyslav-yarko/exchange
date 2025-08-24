from abc import ABC, abstractmethod
from typing import Optional

from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from src.bot.utils.keyboard import Keyboard


class Response(ABC):
    @abstractmethod
    def __init__(self):
        pass


class MessageResponse(Response):
    def __init__(
        self, 
        message: Message, 
        text: str = '', 
        keyboard: Optional[Keyboard] = None, 
        state: Optional[FSMContext] = None):
        self.message = message
        self.keyboard = keyboard
        self.text = text
        self.state = state

    async def answer(self):
        await self.message.answer(
            text=self.text,
            reply_markup=self.keyboard
        )
