import typing
from .api import API


class Vitals:
    def __init__(self, raw_data: dict, api: API):
        self.raw_data = raw_data
        self.api = api

    @property
    def contactor_closed(self) -> bool:
        return self.raw_data["contactor_closed"]

    @property
    def vehicle_connected(self) -> bool:
        return self.raw_data["vehicle_connected"]

    @property
    def session_s(self) -> int:
        return self.raw_data["session_s"]

    @property
    def grid_v(self) -> float:
        return self.raw_data["grid_v"]

    @property
    def grid_hz(self) -> float:
        return self.raw_data["grid_hz"]

    @property
    def vehicle_current_a(self) -> float:
        return self.raw_data["vehicle_current_a"]

    @property
    def currentA_a(self) -> float:
        return self.raw_data["currentA_a"]

    @property
    def currentB_a(self) -> float:
        return self.raw_data["currentB_a"]

    @property
    def currentC_a(self) -> float:
        return self.raw_data["currentC_a"]

    @property
    def currentN_a(self) -> float:
        return self.raw_data["currentN_a"]

    @property
    def voltageA_v(self) -> float:
        return self.raw_data["voltageA_v"]

    @property
    def voltageB_v(self) -> float:
        return self.raw_data["voltageB_v"]

    @property
    def voltageC_v(self) -> float:
        return self.raw_data["voltageC_v"]

    @property
    def relay_coil_v(self) -> float:
        return self.raw_data["relay_coil_v"]

    @property
    def pcba_temp_c(self) -> float:
        return self.raw_data["pcba_temp_c"]

    @property
    def handle_temp_c(self) -> float:
        return self.raw_data["handle_temp_c"]

    @property
    def mcu_temp_c(self) -> float:
        return self.raw_data["mcu_temp_c"]

    @property
    def uptime_s(self) -> int:
        return self.raw_data["uptime_s"]

    @property
    def input_thermopile_uv(self) -> int:
        return self.raw_data["input_thermopile_uv"]

    @property
    def prox_v(self) -> float:
        return self.raw_data["prox_v"]

    @property
    def pilot_high_v(self) -> float:
        return self.raw_data["pilot_high_v"]

    @property
    def pilot_low_v(self) -> float:
        return self.raw_data["pilot_low_v"]

    @property
    def session_energy_wh(self) -> float:
        return self.raw_data["session_energy_wh"]

    @property
    def config_status(self) -> int:
        return self.raw_data["config_status"]

    @property
    def evse_state(self) -> int:
        return self.raw_data["evse_state"]

    @property
    def current_alerts(self) -> typing.List[str]:
        return self.raw_data["current_alerts"]

    async def async_update(self):
        """Update the vitals data."""
        self.raw_data = await self.api.async_request("vitals")
