from typing import Optional

from src.utils.client import JSONClient
from src.enums.crypto import URLEnum


class CryptoClient(JSONClient):
    def __init__(
        self
    ):
        super().__init__(
            base_url=URLEnum.BASE_URL.value
        )
