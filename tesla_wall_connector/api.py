""" Tesla Wall Connector API class """

import asyncio
import json
import re
import socket
from json.decoder import JSONDecodeError

import aiohttp
import async_timeout
import backoff

from .exceptions import (
    WallConnectorConnectionError,
    WallConnectorConnectionTimeoutError,
    WallConnectorDecodeError,
)


class API:
    """This class provides an abstraction for reading data from a Tesla Wall Connector"""

    def __init__(self, host: str, session: aiohttp.ClientSession, timeout: float = 2):
        self.host = host
        self.session = session
        self.timeout = timeout
        self.fix_nan_regex = re.compile(r":\s*\bnan\b", flags=re.IGNORECASE)

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
                    return await self.decode_response(response)
        except asyncio.TimeoutError as ex:
            raise WallConnectorConnectionTimeoutError(
                f"Timeout while connecting to Wall Connector at {self.host}"
            ) from ex
        except (aiohttp.ClientError, socket.gaierror) as ex:
            raise WallConnectorConnectionError(
                f"Error while communicating with Wall Connector at {self.host}: {ex}"
            ) from ex

    async def decode_response(self, response: aiohttp.ClientResponse) -> dict:
        """Decode response applying potentially needed workarounds."""
        raw_body = await response.text()
        # Wall Connector sometimes uses nan in the JSON output, which is not
        # valid JSON. Replace it with null
        raw_body = re.sub(self.fix_nan_regex, ":null ", raw_body)
        try:
            return json.loads(raw_body)
        except JSONDecodeError as ex:
            if len(raw_body) > 0 and raw_body.rstrip()[-1] != "}":
                # Workaround: Wall Connector seems to sometimes return invalid
                # JSON that is just missing the last } character
                # Append that character and retry decoding
                raw_body += "}"
                try:
                    return json.loads(raw_body)
                except JSONDecodeError as ex_:
                    raise WallConnectorDecodeError(
                        (
                            "Error decoding response from wall connector after"
                            " adding closing object character"
                        ),
                        raw_body,
                    ) from ex_
            raise WallConnectorDecodeError(
                "Error decoding response from wall connector", raw_body
            ) from ex
