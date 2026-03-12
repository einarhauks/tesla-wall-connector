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

    @property
    def git_branch(self) -> str:
        """Git branch in the installed firmware build."""
        return self.raw_data["git_branch"]

    @property
    def web_service(self) -> str:
        """Configured Tesla backend web service endpoint."""
        return self.raw_data["web_service"]
