""" Tesla Wall Connector Exceptions """


class WallConnectorError(Exception):
    """Generic WallConnector exception."""


class WallConnectorDecodeError(WallConnectorError):
    """WallConnector exception thrown when decoding a response fails."""

    def __init__(self, message, raw_body):
        """Init Decode error."""
        super().__init__(message)
        self.raw_body = raw_body

    def get_raw_body(self) -> str:
        """Return the raw body of the failing request."""
        return self.raw_body


class WallConnectorEmptyResponseError(WallConnectorError):
    """WallConnector empty API response exception."""


class WallConnectorConnectionError(WallConnectorError):
    """WallConnector connection exception."""


class WallConnectorConnectionTimeoutError(WallConnectorConnectionError):
    """WallConnector connection Timeout exception."""
