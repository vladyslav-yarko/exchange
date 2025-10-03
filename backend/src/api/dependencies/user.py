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
