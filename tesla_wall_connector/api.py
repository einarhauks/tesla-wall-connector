import aiohttp
import asyncio
import async_timeout
import backoff
import socket

import time
from .exceptions import (
    WallConnectorError,
    WallConnectorEmptyResponseError,
    WallConnectorConnectionError,
    WallConnectorConnectionTimeoutError,
)


class API:
    def __init__(self, host: str, session: aiohttp.ClientSession, timeout: float = 2):
        self.host = host
        self.session = session
        self.timeout = timeout

    def get_url(self, endpoint: str):
        return "http://{}/api/1/{}".format(self.host, endpoint)

    @backoff.on_exception(
        backoff.expo,
        (WallConnectorConnectionTimeoutError, WallConnectorConnectionError),
        max_tries=3,
    )
    async def async_request(self, endpoint: str) -> dict:
        try:
            async with async_timeout.timeout(self.timeout):
                async with self.session.get(self.get_url(endpoint)) as response:
                    response.raise_for_status()
                    return await response.json()
        except asyncio.TimeoutError:
            raise WallConnectorConnectionTimeoutError(
                f"Timeout while connecting to Wall Connector at {self.host}"
            )
        except (aiohttp.ClientError, socket.gaierror) as ex:
            raise WallConnectorConnectionError(
                f"Error while communicating with Wall Connector at {self.host}: {ex}"
            )
