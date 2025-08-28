from typing import Optional

from src.utils.client import JSONClient
from src.enums.currency import URLEnum
from src.config import settings


class CurrencyClient(JSONClient):
    def __init__(
        self
    ):
        super().__init__(
            base_url=URLEnum.BASE_URL.value
        )
