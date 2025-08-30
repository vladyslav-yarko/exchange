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
        
    @http_session
    async def get_price(self, data: CryptoPriceBody) -> Union[dict, tuple[int, str]]:
        symbol1 = data.get("symbol1")
        symbol2 = data.get("symbol2")
        symbol = symbol1 + symbol2
        symbol_data = await self.crypto_repo(self.session).get_one_by_symbol(symbol)
        if not symbol_data:
            return (422, "Symbol combination has not found")
        client_data = await self.client.get_symbol_price(symbol)
        if not client_data:
            return (422, "Symbol combination has not found")
        data = dict()
        data["symbol"] = symbol
        price = float(client_data.get("price"))
        data["price"] = format_decimal(price)  
        return data
        
    @transaction
    async def create_one(self, data: CryptoBody) -> Union[dict, tuple[int, str]]:
        symbol = data.get("symbol1") + data.get('symbol2')
        d = await self.crypto_repo(self.session).get_one_by_symbol(symbol)
        if d:
            return (422, "Symbols combination has already found")
        data['symbol'] = symbol
        return await super().create_one(data)
    
    @transaction
    async def update_one(self, id: Union[int, uuid.UUID], data: CryptoBody) -> Union[dict, tuple[int, str]]:
        symbol = data.get("symbol1") + data.get('symbol2')
        d = await self.crypto_repo(self.session).get_one_by_symbol(symbol)
        if d:
            return (422, "Symbols combination has already found")
        data['symbol'] = symbol
        return await super().update_one(id, data)
    
    @transaction
    async def delete_one(self, id: Union[int, uuid.UUID]) -> Union[dict, tuple[int, str]]:
        return await super().delete_one(id)
    
    async def get_subscribe_one(self, user_id: Union[int, uuid.UUID], symbol: str) -> Union[dict, tuple[int, str]]:
        subscribe = await self.crypto_subscribes_repo(self.session).get_one_by_id_symbol(user_id, symbol)
        if not subscribe:
            return (422, "Symbols combination has not found")
        return subscribe
