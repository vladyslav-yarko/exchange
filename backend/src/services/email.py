from typing import Union
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.schemas.email import EmailBody, ValidateEmailBody, IsVerifiedEmailBody
from src.utils.repository import Repository
from src.utils.code import code_manager
from src.utils.email import email_manager
from src.enums.validation import ValidationEnum


class EmailService(Service):
    def __init__(
        self,
        session: AsyncSession,
        user_repo: Repository
        ):
        super().__init__(session)
        self.user_repo = user_repo
        self.code_manager = code_manager
        self.email_manager = email_manager
