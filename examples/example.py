import os
import sys
  
# append the path of the parent directory
sys.path.append("..")

from tesla_wall_connector import WallConnector

def getenv(var):
    val = os.getenv(var)
    if val is None:
        raise ValueError(f"{var} must be set")
    return val

ip = getenv("WALLCONNECTOR_IP")

import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        api = WallConnector(ip, session)
        print("---- Vitals ----")
        vitals = await api.async_get_vitals()

        print("contactor_closed: {}".format(vitals.contactor_closed))
        print("vehicle_connected: {}".format(vitals.vehicle_connected))
        print("session_s: {}s".format(vitals.session_s))
        print("grid_v: {}V".format(vitals.grid_v))
        print("grid_hz: {}Hz".format(vitals.grid_hz))
        print("vehicle_current_a: {}A".format(vitals.vehicle_current_a))
        print("currentA_a: {}A".format(vitals.currentA_a))
        print("currentB_a: {}A".format(vitals.currentB_a))
        print("currentC_a: {}A".format(vitals.currentC_a))
        print("currentN_a: {}A".format(vitals.currentN_a))
        print("voltageA_v: {}V".format(vitals.voltageA_v))
        print("voltageB_v: {}V".format(vitals.voltageB_v))
        print("voltageC_v: {}V".format(vitals.voltageC_v))
        print("relay_coil_v: {}V".format(vitals.relay_coil_v))
        print("pcba_temp_c: {}°C".format(vitals.pcba_temp_c))
        print("handle_temp_c: {}°C".format(vitals.handle_temp_c))
        print("mcu_temp_c: {}°C".format(vitals.mcu_temp_c))
        print("uptime_s: {}s".format(vitals.uptime_s))
        print("input_thermopile_uv: {}".format(vitals.input_thermopile_uv))
        print("prox_v: {}V".format(vitals.prox_v))
        print("pilot_high_v: {}V".format(vitals.pilot_high_v))
        print("pilot_low_v: {}V".format(vitals.pilot_low_v))
        print("session_energy_wh: {}Wh".format(vitals.session_energy_wh))
        print("config_status: {}".format(vitals.config_status))
        print("evse_state: {}".format(vitals.evse_state))
        print("current_alerts: {}".format(vitals.current_alerts))

        await asyncio.sleep(2)

        await vitals.async_update()
        print("uptime_s: {}s".format(vitals.uptime_s))


        print("---- Lifetime ----")
        lifetime = await api.async_get_lifetime()
        
        print("contactor_cycles: {}".format(lifetime.contactor_cycles))
        print("contactor_cycles_loaded: {}".format(lifetime.contactor_cycles_loaded))
        print("alert_count: {}".format(lifetime.alert_count))
        print("thermal_foldbacks: {}".format(lifetime.thermal_foldbacks))
        print("avg_startup_temp: {}°C".format(lifetime.avg_startup_temp))
        print("charge_starts: {}".format(lifetime.charge_starts))
        print("energy_wh: {}Wh".format(lifetime.energy_wh))
        print("connector_cycles: {}".format(lifetime.connector_cycles))
        print("uptime_s: {}s".format(lifetime.uptime_s))
        print("charging_time_s: {}s".format(lifetime.charging_time_s))

        await asyncio.sleep(2)

        await lifetime.async_update()
        print("uptime_s: {}s".format(lifetime.uptime_s))


asyncio.run(main())
