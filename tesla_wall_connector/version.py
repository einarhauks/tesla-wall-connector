""" Version Data class for Tesla Wall Connector """


class Version:
    """Object holding version information about a Tesla Wall Connector"""

    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

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
