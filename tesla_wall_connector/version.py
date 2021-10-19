""" Version Data class for Tesla Wall Connector """
from .api import API


class Version:
    """Object holding version information about a Tesla Wall Connector"""

    def __init__(self, raw_data: dict, api: API):
        self.raw_data = raw_data
        self.api = api

    @property
    def firmware_version(self) -> str:
        """Firmware version"""
        return self.raw_data["firmware_version"]

    @property
    def part_number(self) -> str:
        """Part number"""
        return self.raw_data["part_number"]

    @property
    def serial_number(self) -> str:
        """Serial Number"""
        return self.raw_data["serial_number"]

    async def async_update(self):
        """Update the version data."""
        self.raw_data = await self.api.async_request("version")
