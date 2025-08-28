from typing import Optional

from src.utils.client import JSONClient
from src.constants.oauth2 import GOOGLE_TOKEN_BASE_URL, GOOGLE_TOKEN_ENDPOINT_URl, GOOGLE_REDIRECT_URI
from src.config import settings


class Oauth2Client(JSONClient):
    def __init__(
        self
    ):
        super().__init__(
            base_url=GOOGLE_TOKEN_BASE_URL
        )
