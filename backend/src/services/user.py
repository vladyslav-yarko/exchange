from typing import Union, Optional, Any
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository, transaction
from src.utils.password import pw_manager
from src.utils.jwt import jwt_manager
from src.utils.oauth2 import oauth2
from src.utils.client import JSONClient, http_session
from src.schemas.user import UserBody, LoginUserBody, UpdateUserBody
from src.enums.user import RoleEnum, TokenEnum
from src.clients import Oauth2Client


class UserService(Service):
    def __init__(
        self,
        session: AsyncSession,
        oauth2_client: JSONClient,
        user_repo: Repository,
        telegram_user_repo: Repository
    ):
        super().__init__(session)
        self.repo = user_repo
        self.user_repo = user_repo
        self.telegram_user_repo = telegram_user_repo
        self.jwt = jwt_manager
        self.pw = pw_manager
        self.oauth_manager = oauth2
        self.client = oauth2_client
    
    @transaction
    async def create_one(self, data: UserBody) -> Union[dict, tuple[int, str]]:
        user = await self.user_repo(self.session).get_one_by_username(data.get('username'))
        if user:
            return (422, "Username has already found")
        user = await self.user_repo(self.session).get_one_by_email(data.get("email"))
        if user:
            return (422, "Email has already found")
        password = self.pw.hash_password(data.get('password'))
        data["password"] = password
        return await super().create_one(data)
