# pylint: disable=invalid-name
#   in order to use the attribute names as they appear in the Tesla API
# pylint: disable=too-many-public-methods
#   this object has a lot of attributes in the Tesla API, therefore we need many public methods
""" Vitals Data class for Tesla Wall Connector """
import typing


class Vitals:
    """Object holding 'vitals' data for a Tesla Wall Connector"""

    def __init__(self, raw_data: dict):
        """Return a new Vitals object from Tesla Wall Connector API response"""
        self.raw_data = raw_data

    @property
    def contactor_closed(self) -> bool:
        """Is the contector closed"""
        return self.raw_data["contactor_closed"]

    @property
    def vehicle_connected(self) -> bool:
        """Is the vehicle connected"""
        return self.raw_data["vehicle_connected"]

    @property
    def session_s(self) -> int:
        """Current session time in seconds"""
        return self.raw_data["session_s"]

    @property
    def grid_v(self) -> float:
        """Measured grid voltage"""
        return self.raw_data["grid_v"]

    @property
    def grid_hz(self) -> float:
        """Measured grid frequency"""
        return self.raw_data["grid_hz"]

    @property
    def vehicle_current_a(self) -> float:
        """Measured vehicle current"""
        return self.raw_data["vehicle_current_a"]

    @property
    def currentA_a(self) -> float:
        """Measured current on phase A"""
        return self.raw_data["currentA_a"]

    @property
    def currentB_a(self) -> float:
        """Measured current on phase B"""
        return self.raw_data["currentB_a"]

    @property
    def currentC_a(self) -> float:
        """Measured current on phase C"""
        return self.raw_data["currentC_a"]

    @property
    def currentN_a(self) -> float:
        """Measured current on neutral"""
        return self.raw_data["currentN_a"]

    @property
    def voltageA_v(self) -> float:
        """Measured voltage on phase A"""
        return self.raw_data["voltageA_v"]

    @property
    def voltageB_v(self) -> float:
        """Measured voltage on phase B"""
        return self.raw_data["voltageB_v"]

    @property
    def voltageC_v(self) -> float:
        """Measured voltage on phase C"""
        return self.raw_data["voltageC_v"]

    @property
    def relay_coil_v(self) -> float:
        """Relay coil voltage"""
        return self.raw_data["relay_coil_v"]

    @property
    def pcba_temp_c(self) -> float:
        """PCBA temperature"""
        return self.raw_data["pcba_temp_c"]

    @property
    def handle_temp_c(self) -> float:
        """Handle Temperature"""
        return self.raw_data["handle_temp_c"]

    @property
    def mcu_temp_c(self) -> float:
        """MCU Temperature"""
        return self.raw_data["mcu_temp_c"]

    @property
    def uptime_s(self) -> int:
        """Uptime in seconds"""
        return self.raw_data["uptime_s"]

    @property
    def input_thermopile_uv(self) -> int:
        """Input thermopile UV"""
        return self.raw_data["input_thermopile_uv"]

    @property
    def prox_v(self) -> float:
        """PROX V"""
        return self.raw_data["prox_v"]

    @property
    def pilot_high_v(self) -> float:
        """Pilot signal high voltage"""
        return self.raw_data["pilot_high_v"]

    @property
    def pilot_low_v(self) -> float:
        """Pilot signal low voltage"""
        return self.raw_data["pilot_low_v"]

    @property
    def session_energy_wh(self) -> float:
        """Amount of energy delivered by the wall connector during this session"""
        return self.raw_data["session_energy_wh"]

    @property
    def config_status(self) -> int:
        """Config status"""
        return self.raw_data["config_status"]

    @property
    def evse_state(self) -> int:
        """State of the Wall Connector"""
        return self.raw_data["evse_state"]

    @property
    def current_alerts(self) -> typing.List[str]:
        """Current alerts"""
        return self.raw_data["current_alerts"]
