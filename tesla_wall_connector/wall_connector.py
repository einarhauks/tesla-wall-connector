"""Asynchronous Python client for Tesla Wall Connector"""

from aiohttp import ClientSession

from .api import API
from .lifetime import Lifetime
from .version import Version
from .vitals import Vitals
from .wifi_status import WifiStatus


class WallConnector:
    """Main class for reading data from a Tesla Wall Connector"""

    def __init__(
        self,
        host: str,
        timeout: float = 1,
        session: ClientSession = None,
        split_phase: bool = False,
    ):
        if session is None:
            session = ClientSession()
            self._session = session
        self.api = API(host, session, timeout)
        self.split_phase = split_phase

    async def async_get_vitals(self) -> dict:
        """Get 'vitals' data"""
        return Vitals(
            await self.api.async_request("vitals"),
            split_phase=self.split_phase,
        )

    async def async_get_lifetime(self) -> dict:
        """Get 'lifetime' data"""
        return Lifetime(await self.api.async_request("lifetime"))

    async def async_get_version(self) -> dict:
        """Get version information"""
        return Version(await self.api.async_request("version"))

    async def async_get_wifi_status(self) -> dict:
        """Get wifi status information"""
        return WifiStatus(await self.api.async_request("wifi_status"))

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_exc_info) -> None:
        if self._session:
            await self._session.close()
