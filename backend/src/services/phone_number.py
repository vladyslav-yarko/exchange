from typing import Union
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository
from src.schemas.phone_number import PhoneNumberBody, ValidatePhoneNumberBody, IsVerifiedPhoneNumberBody
from src.utils.code import code_manager
from src.bot.bot import bot
from src.enums.validation import ValidationEnum

class PhoneNumberService(Service):
    def __init__(
        self,
        session: AsyncSession,
        telegram_user_repo: Repository,
        user_repo: Repository
        ):
        super().__init__(session)
        self.telegram_user_repo = telegram_user_repo
        self.user_repo = user_repo
        self.code_manager = code_manager
