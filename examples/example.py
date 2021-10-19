""" Example showing usage of this library """
# pylint: disable=missing-function-docstring

import os
import sys

import asyncio
import aiohttp
from tesla_wall_connector import WallConnector

sys.path.append("..")


def getenv(var):
    val = os.getenv(var)
    if val is None:
        raise ValueError(f"{var} must be set")
    return val


ip = getenv("WALLCONNECTOR_IP")


async def main():

    async with aiohttp.ClientSession() as session:
        api = WallConnector(ip, 0.0001, session)
        print("---- Vitals ----")
        vitals = await api.async_get_vitals()

        print(f"contactor_closed: {vitals.contactor_closed}")
        print(f"vehicle_connected: {vitals.vehicle_connected}")
        print(f"session_s: {vitals.session_s}s")
        print(f"grid_v: {vitals.grid_v}V")
        print(f"grid_hz: {vitals.grid_hz}Hz")
        print(f"vehicle_current_a: {vitals.vehicle_current_a}A")
        print(f"currentA_a: {vitals.currentA_a}A")
        print(f"currentB_a: {vitals.currentB_a}A")
        print(f"currentC_a: {vitals.currentC_a}A")
        print(f"currentN_a: {vitals.currentN_a}A")
        print(f"voltageA_v: {vitals.voltageA_v}V")
        print(f"voltageB_v: {vitals.voltageB_v}V")
        print(f"voltageC_v: {vitals.voltageC_v}V")
        print(f"relay_coil_v: {vitals.relay_coil_v}V")
        print(f"pcba_temp_c: {vitals.pcba_temp_c}°C")
        print(f"handle_temp_c: {vitals.handle_temp_c}°C")
        print(f"mcu_temp_c: {vitals.mcu_temp_c}°C")
        print(f"uptime_s: {vitals.uptime_s}s")
        print(f"input_thermopile_uv: {vitals.input_thermopile_uv}")
        print(f"prox_v: {vitals.prox_v}V")
        print(f"pilot_high_v: {vitals.pilot_high_v}V")
        print(f"pilot_low_v: {vitals.pilot_low_v}V")
        print(f"session_energy_wh: {vitals.session_energy_wh}Wh")
        print(f"config_status: {vitals.config_status}")
        print(f"evse_state: {vitals.evse_state}")
        print(f"current_alerts: {vitals.current_alerts}")

        await asyncio.sleep(2)

        await vitals.async_update()
        print(f"uptime_s: {vitals.uptime_s}s")

        print("---- Lifetime ----")
        lifetime = await api.async_get_lifetime()

        print(f"contactor_cycles: {lifetime.contactor_cycles}")
        print(f"contactor_cycles_loaded: {lifetime.contactor_cycles_loaded}")
        print(f"alert_count: {lifetime.alert_count}")
        print(f"thermal_foldbacks: {lifetime.thermal_foldbacks}")
        print(f"avg_startup_temp: {lifetime.avg_startup_temp}°C")
        print(f"charge_starts: {lifetime.charge_starts}")
        print(f"energy_wh: {lifetime.energy_wh}Wh")
        print(f"connector_cycles: {lifetime.connector_cycles}")
        print(f"uptime_s: {lifetime.uptime_s}s")
        print(f"charging_time_s: {lifetime.charging_time_s}s")

        await asyncio.sleep(2)

        await lifetime.async_update()
        print(f"uptime_s: {lifetime.uptime_s}s")


asyncio.run(main())
