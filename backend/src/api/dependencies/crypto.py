from typing import Annotated, Callable, Awaitable

from fastapi import Depends, Path, HTTPException

from src.api.utils.dependency_factory import DependencyFactory
from src.api.dependencies.db import DBSession
from src.repositories import CryptoRepository, CryptoSubscribeRepository, UserRepository
from src.clients import CryptoClient
from src.services import CryptoService
from src.schemas.crypto import CryptoBody, CryptoPublic, CryptoSPublic, CryptoSubscribeBody, CryptoSubscribePublic, CryptoSubscribesPublic, CryptoPricePublic, CryptoPriceBody
from src.models import User
from src.utils.validation import check_upper_case


async def service_dep(session: DBSession) -> CryptoService:
    return CryptoService(
        session=session,
        crypto_client=CryptoClient(),
        crypto_repo=CryptoRepository,
        crypto_subscribes_repo=CryptoSubscribeRepository,
        user_repo=UserRepository
    )


class CryptoDependencyFactory(DependencyFactory):
    def __init__(self):
        super().__init__(
            service_dep=service_dep,
            SchemaBody=CryptoBody,
            SchemaPublic=CryptoPublic,
            DataSchemaPublic=CryptoSPublic
        )
        
    def symbol_dep(self) -> Callable[[], Awaitable[str]]:
        async def dep(
            symbol: str = Path(..., examples=["BTCUSDT"], min_length=2, max_length=50, description="Unique symbol combination. 💫")
            ) -> str:
            try:
                check_upper_case(symbol)
            except ValueError:
                raise HTTPException(
                    status_code=422,
                    detail="Symbol must be in upper case"
                )
            return symbol
        return dep

    def get_price_dep(self) -> Callable[[], Awaitable[CryptoPricePublic]]:
        async def dep(
            body: CryptoPriceBody,
            user: User = Depends(self.token_dep()),
            service: CryptoService = Depends(self.service_dep)) -> CryptoPricePublic:
            data = await service.get_price(body.model_dump())
            self.check_for_exception(data)
            response = CryptoPricePublic(**data)
            return response
        return dep

    def subscribe_get_dep(self) -> Callable[[], Awaitable[CryptoSubscribesPublic]]:
        async def dep(
            user: User = Depends(self.token_dep()),
            page: int = Depends(self.page_dep()),
            service: CryptoService = Depends(self.service_dep)) -> CryptoSubscribesPublic:
            data = await service.subscribes_get(user.id, page)
            response = CryptoSubscribesPublic(**data)
            return response
        return dep
