import requests
from typing import Dict, Any, Optional, Union, List
from enum import Enum

from tenacity import wait_fixed, stop_after_attempt, retry


class SortOrder(Enum):
    ASC = "asc"
    DESC = "desc"

class CoinSortBy(Enum):
    CREATED_AT = "createdAt"
    MARKET_CAP = "marketCap"
    VOLUME_24H = "volume24h"
    TOTAL_VOLUME = "totalVolume"
    UNIQUE_HOLDERS = "uniqueHolders"

class ProfileSortBy(Enum):
    CREATED_AT = "createdAt"
    BALANCE = "balance"
    VALUE = "value"

class FilterType(Enum):
    TRENDING = "trending"
    NEW = "new"
    TOP = "top"

class ChainId(Enum):
    ETHEREUM = 1
    BASE = 8453
    ZORA = 7777777
    OPTIMISM = 10
    ARBITRUM = 42161



class ZoraPy:
    """Simple and flexible Zora Client"""

    def __init__(self, api_key: str, base_url: str = "https://api-sdk.zora.engineering"):
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "Content-Type": "application/json",
            "api-key": api_key
        }

    @retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
    def call(self, endpoint: str, method: str = "GET", params: Optional[Dict] = None, data: Optional[Dict] = None) -> \
    Dict[str, Any]:
        """
        Generic method to call any Zora API endpoint

        Args:
            endpoint: API endpoint (e.g., 'profile', 'coin', 'explore')
            method: HTTP method (GET, POST, etc.)
            params: Query parameters
            data: Request body data

        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=data,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()