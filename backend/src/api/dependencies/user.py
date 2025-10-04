from typing import Annotated, Callable, Awaitable, Optional, Union
import uuid

from fastapi import Depends, HTTPException, status, Cookie, Response, Path
from fastapi.responses import RedirectResponse

from src.api.utils.dependency_factory import DependencyFactory
from src.api.dependencies.db import DBSession
from src.clients import Oauth2Client
from src.repositories import UserRepository, TelegramUserRepository
from src.services import UserService
from src.schemas.user import UserBody, UserPublic, UsersPublic, CallbackGoogleBody, CallbackGooglePublic, LoginUserBody, LoginUserPublic, RefreshPublic, UpdateUserBody, LogoutUserPublic
from src.enums.user import TokenEnum
from src.models import User as UserModel


async def service_dep(session: DBSession) -> UserService:
    return UserService(
        session=session,
        oauth2_client=Oauth2Client(),
        user_repo=UserRepository,
        telegram_user_repo=TelegramUserRepository
    )


class UserDependencyFactory(DependencyFactory):
    def __init__(self):
        super().__init__(
            service_dep=service_dep,
            SchemaBody=UserBody,
            SchemaPublic=UserPublic,
            DataSchemaPublic=UsersPublic,
            PhoneNumberBody=UpdateUserBody,
            EmailBody=UpdateUserBody
        )
        
    def refresh_token_dep(self) -> uuid.UUID:
        async def dep(
            refreshToken: Optional[uuid.UUID] = Cookie(None, examples=[None], description="Refresh token id. (You do not need to pass it). 💫")            
        ) -> uuid.UUID:
            return refreshToken
        return dep
