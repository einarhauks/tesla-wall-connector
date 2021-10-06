from aiohttp import ClientSession, ClientResponse

class API:
    def __init__(self, host: str, session: ClientSession):
        self.host = host
        self.session = session

    def get_url(self, endpoint : str):
        return "http://{}/api/1/{}".format(self.host, endpoint)

    async def async_request(self, endpoint : str) -> dict:
        async with self.session.get(self.get_url(endpoint)) as response:
            response.raise_for_status()
            return await response.json()