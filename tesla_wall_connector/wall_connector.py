from aiohttp import ClientSession
from .vitals import Vitals
from .lifetime import Lifetime
from .api import API

class WallConnector:
    def __init__(self, host: str, session: ClientSession):
        self.api = API(host, session)

    async def async_get_vitals(self) -> dict:
        return Vitals(await self.api.async_request("vitals"), self.api)

    async def async_get_lifetime(self) -> dict:
        return Lifetime(await self.api.async_request("lifetime"), self.api)
