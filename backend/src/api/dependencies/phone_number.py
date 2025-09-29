from typing import Callable, Awaitable, Optional, Annotated

from fastapi import Depends, Response, Cookie, HTTPException

from src.api.dependencies.db import DBSession
from src.schemas.phone_number import PhoneNumberBody, PhoneNumberPublic, ValidatePhoneNumberBody, ValidatePhoneNumberPublic, IsVerifiedPhoneNumberBody, IsVerifiedPhoneNumberPublic
from src.repositories import TelegramUserRepository, UserRepository
from src.api.utils.dependency_factory import DependencyFactory
from src.services import PhoneNumberService
from src.enums.validation import ValidationEnum
from src.models import User


async def service_dep(session: DBSession) -> PhoneNumberService:
    return PhoneNumberService(
        session=session,
        telegram_user_repo=TelegramUserRepository,
        user_repo=UserRepository
    )


class PhoneNumberDependencyFactory(DependencyFactory):
    def __init__(self):
        super().__init__(
            service_dep=service_dep,
        )
