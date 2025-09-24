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
    def __init__(self):
        super().__init__(
            service_dep=service_dep,
        )
        
    def send_dep(self) -> Callable[[], Awaitable[EmailPublic]]:
        async def dep(
            response: Response,
            body: EmailBody,
            service: EmailService = Depends(self.service_dep)) -> EmailPublic:
            data = await service.send(body.model_dump())
            self.check_for_exception(data)
            self.set_cookie(response, "email", data[1], ValidationEnum.EXPIRE_TIME.value) 
            return EmailPublic(**data[0])
        return dep
