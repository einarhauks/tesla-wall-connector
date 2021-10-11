from .api import API


class Version:
    def __init__(self, raw_data: dict, api: API):
        self.raw_data = raw_data
        self.api = api

    @property
    def firmware_version(self) -> str:
        return self.raw_data["firmware_version"]

    @property
    def part_number(self) -> str:
        return self.raw_data["part_number"]

    @property
    def serial_number(self) -> str:
        return self.raw_data["serial_number"]

    async def async_update(self):
        """Update the version data."""
        self.raw_data = await self.api.async_request("version")
