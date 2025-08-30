from typing import Union, Optional
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository, transaction
from src.utils.client import JSONClient, http_session
from src.utils.decimal import format_decimal
from src.schemas.currency import CurrencyBody, CurrencySubscribeBody, CurrencyPriceBody


class CurrencyService(Service):
    def __init__(
        self,
        session: AsyncSession,
        currency_client: JSONClient,
        currency_repo: Repository,
        currency_subscribes_repo: Repository,
        user_repo: Repository
    ):
        super().__init__(session)
        self.repo = currency_repo
        self.currency_repo = currency_repo
        self.currency_subscribes_repo = currency_subscribes_repo
        self.user_repo = user_repo
        self.client = currency_client
