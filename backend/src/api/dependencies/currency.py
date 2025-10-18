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
