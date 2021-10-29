""" Lifetime Data class for Tesla Wall Connector """


class Lifetime:
    """Object holding lifetime data for Tesla Wall Connector"""

    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    @property
    def contactor_cycles(self) -> int:
        """Contactor cycles"""
        return self.raw_data["contactor_cycles"]

    @property
    def contactor_cycles_loaded(self) -> int:
        """Contactor cycles Loaded"""
        return self.raw_data["contactor_cycles_loaded"]

    @property
    def alert_count(self) -> int:
        """Alert Count"""
        return self.raw_data["alert_count"]

    @property
    def thermal_foldbacks(self) -> int:
        """Thermal foldbacks"""
        return self.raw_data["thermal_foldbacks"]

    @property
    def avg_startup_temp(self) -> float:
        """Average startup Temperature"""
        return self.raw_data["avg_startup_temp"]

    @property
    def charge_starts(self) -> int:
        """Number of started charges"""
        return self.raw_data["charge_starts"]

    @property
    def energy_wh(self) -> int:
        """Total energy delivered in Wh"""
        return self.raw_data["energy_wh"]

    @property
    def connector_cycles(self) -> int:
        """Connector cycles"""
        return self.raw_data["connector_cycles"]

    @property
    def uptime_s(self) -> int:
        """Uptime in seconds"""
        return self.raw_data["uptime_s"]

    @property
    def charging_time_s(self) -> int:
        """Total Charging time in seconds"""
        return self.raw_data["charging_time_s"]
