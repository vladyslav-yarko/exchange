from typing import Union, Optional
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository, transaction
from src.utils.client import JSONClient, http_session
from src.utils.decimal import format_decimal
from src.schemas.crypto import CryptoBody, CryptoSubscribeBody, CryptoPriceBody
from src.utils.logger import logger


class CryptoService(Service):
    def __init__(
        self,
        session: AsyncSession,
        crypto_client: JSONClient,
        crypto_repo: Repository,
        crypto_subscribes_repo: Repository,
        user_repo: Repository
    ):
        super().__init__(session)
        self.repo = crypto_repo
        self.crypto_repo = crypto_repo
        self.crypto_subscribes_repo = crypto_subscribes_repo
        self.user_repo = user_repo
        self.client = crypto_client
