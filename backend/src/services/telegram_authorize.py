from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository, transaction


class TelegramAuthorizeService(Service):
    def __init__(
        self,
        session: AsyncSession,
        telegram_user_repo: Repository
        ):
        super().__init__(session)
        self.telegram_user_repo = telegram_user_repo
        self.repo = telegram_user_repo
