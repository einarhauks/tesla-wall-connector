"""Wifi status data class for Tesla Wall Connector."""
import base64
import binascii


class WifiStatus:
    """Object holding wifi status data for Tesla Wall Connector."""

    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    @property
    def wifi_ssid(self) -> str:
        """Wifi SSID reported by the Wall Connector.

        Tesla reports this value base64-encoded, but some firmware variants
        may already return plaintext. Decode when possible and otherwise return
        the raw value.
        """
        raw_ssid = self.raw_data["wifi_ssid"]
        if not raw_ssid:
            return raw_ssid
        try:
            return base64.b64decode(raw_ssid, validate=True).decode("utf-8")
        except (binascii.Error, UnicodeDecodeError, ValueError):
            return raw_ssid

    @property
    def wifi_signal_strength(self) -> int:
        """Wifi signal strength."""
        return self.raw_data["wifi_signal_strength"]

    @property
    def wifi_rssi(self) -> int:
        """Wifi received signal strength indicator."""
        return self.raw_data["wifi_rssi"]

    @property
    def wifi_snr(self) -> int:
        """Wifi signal-to-noise ratio."""
        return self.raw_data["wifi_snr"]

    @property
    def wifi_connected(self) -> bool:
        """Whether wifi is connected."""
        return self.raw_data["wifi_connected"]

    @property
    def wifi_infra_ip(self) -> str:
        """Wifi infrastructure IP address."""
        return self.raw_data["wifi_infra_ip"]

    @property
    def internet(self) -> bool:
        """Whether Wall Connector has internet connectivity."""
        return self.raw_data["internet"]

    @property
    def wifi_mac(self) -> str:
        """Wifi MAC address."""
        return self.raw_data["wifi_mac"]
