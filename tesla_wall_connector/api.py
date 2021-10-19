""" Tesla Wall Connector API class """

import asyncio
import socket
import async_timeout
import aiohttp
import backoff

from .exceptions import (
    WallConnectorConnectionError,
    WallConnectorConnectionTimeoutError,
)


class API:
    """This class provides an abstraction for reading data from a Tesla Wall Connector"""

    def __init__(self, host: str, session: aiohttp.ClientSession, timeout: float = 2):
        self.host = host
        self.session = session
        self.timeout = timeout

    def get_url(self, endpoint: str):
        """Construct a Wall Charger URL for a specified endpoint"""
        return f"http://{self.host}/api/1/{endpoint}"

    @backoff.on_exception(
        backoff.expo,
        (WallConnectorConnectionTimeoutError, WallConnectorConnectionError),
        max_tries=3,
    )
    async def async_request(self, endpoint: str) -> dict:
        """Make an asynchronous request to a Tesla Wall Connector endpoint
        Args:
            endpoint: Endpoint string such as 'vitals' or 'lifetime'

        Raises:
            WallConnectorConnectionTimeoutError: The connection timed out
            WallConnectorConnectionError: Any communication error

        Returns:
            Data for the given endpoint
        """
        try:
            async with async_timeout.timeout(self.timeout):
                async with self.session.get(self.get_url(endpoint)) as response:
                    response.raise_for_status()
                    return await response.json()
        except asyncio.TimeoutError as ex:
            raise WallConnectorConnectionTimeoutError(
                f"Timeout while connecting to Wall Connector at {self.host}"
            ) from ex
        except (aiohttp.ClientError, socket.gaierror) as ex:
            raise WallConnectorConnectionError(
                f"Error while communicating with Wall Connector at {self.host}: {ex}"
            ) from ex
