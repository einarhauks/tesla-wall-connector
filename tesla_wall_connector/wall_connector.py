from aiohttp import ClientSession, ClientTimeout
from .vitals import Vitals
from .lifetime import Lifetime
from .version import Version
from .api import API


class WallConnector:
    def __init__(self, host: str, timeout: float = 1, session: ClientSession = None):
        if session is None:
            session = ClientSession()
        self.api = API(host, session, timeout)

    async def async_get_vitals(self) -> dict:
        return Vitals(await self.api.async_request("vitals"), self.api)

    async def async_get_lifetime(self) -> dict:
        return Lifetime(await self.api.async_request("lifetime"), self.api)

    async def async_get_version(self) -> dict:
        return Version(await self.api.async_request("version"), self.api)
