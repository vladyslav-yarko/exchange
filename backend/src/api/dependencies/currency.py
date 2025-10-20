from typing import Annotated, Callable, Awaitable

from fastapi import Depends, Path, HTTPException

from src.api.utils.dependency_factory import DependencyFactory
from src.api.dependencies.db import DBSession
from src.repositories import CurrencyRepository, CurrencySubscribeRepository, UserRepository
from src.clients import CurrencyClient
from src.services import CurrencyService
from src.schemas.currency import CurrencyBody, CurrencyPublic, CurrenciesPublic, CurrencySubscribeBody, CurrencySubscribePublic, CurrencySubscribesPublic, CurrencyPricePublic, CurrencyPriceBody
from src.models import User
from src.utils.validation import check_upper_case


async def service_dep(session: DBSession) -> CurrencyService:
    return CurrencyService(
        session=session,
        currency_client=CurrencyClient(),
        currency_repo=CurrencyRepository,
        currency_subscribes_repo=CurrencySubscribeRepository,
        user_repo=UserRepository
    )


class CurrencyDependencyFactory(DependencyFactory):
    def __init__(self):
        super().__init__(
            service_dep=service_dep,
            SchemaBody=CurrencyBody,
            SchemaPublic=CurrencyPublic,
            DataSchemaPublic=CurrenciesPublic
        )
        
    def symbol_dep(self) -> Callable[[], Awaitable[str]]:
        async def dep(
            symbol: str = Path(..., examples=["USDUAH"], min_length=2, max_length=50, description="Unique symbol combination. 💫")
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
    
    def get_price_dep(self) -> Callable[[], Awaitable[CurrencyPricePublic]]:
        async def dep(
            body: CurrencyPriceBody,
            user: User = Depends(self.token_dep()),
            service: CurrencyService = Depends(self.service_dep)) -> CurrencyPricePublic:
            data = await service.get_price(body.model_dump())
            self.check_for_exception(data)
            response = CurrencyPricePublic(**data)
            return response
        return dep
        
    def subscribe_get_dep(self) -> Callable[[], Awaitable[CurrencySubscribesPublic]]:
        async def dep(
            user: User = Depends(self.token_dep()),
            page: int = Depends(self.page_dep()),
            service: CurrencyService = Depends(self.service_dep)) -> CurrencySubscribesPublic:
            data = await service.subscribes_get(user.id, page)
            response = CurrencySubscribesPublic(**data)
            return response
        return dep
