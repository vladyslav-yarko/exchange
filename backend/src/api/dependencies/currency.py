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
