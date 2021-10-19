""" Tesla Wall Connector Exceptions """


class WallConnectorError(Exception):
    """Generic WallConnector exception."""


class WallConnectorEmptyResponseError(Exception):
    """WallConnector empty API response exception."""


class WallConnectorConnectionError(WallConnectorError):
    """WallConnector connection exception."""


class WallConnectorConnectionTimeoutError(WallConnectorConnectionError):
    """WallConnector connection Timeout exception."""
