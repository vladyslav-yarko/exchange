from typing import Annotated, Callable, Awaitable, Optional

from fastapi import Depends, HTTPException, Response, Cookie, HTTPException

from src.services import EmailService
from src.api.dependencies.db import DBSession
from src.repositories import UserRepository
from src.schemas.email import EmailPublic, EmailBody, ValidateEmailPublic, ValidateEmailBody, IsVerifiedEmailBody, IsVerifiedEmailPublic
from src.api.utils.dependency_factory import DependencyFactory
from src.enums.validation import ValidationEnum


async def service_dep(session: DBSession) -> EmailService:
    return EmailService(
        session=session,
        user_repo=UserRepository
    )


class EmailDependencyFactory(DependencyFactory):
    pass
