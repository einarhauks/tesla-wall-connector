# pylint: disable=missing-function-docstring
""" Tests for Tesla Wall Connector API """
import asyncio
import aiohttp
import pytest

from tesla_wall_connector.exceptions import (
    WallConnectorConnectionError,
    WallConnectorConnectionTimeoutError,
    WallConnectorDecodeError,
)

from tesla_wall_connector import WallConnector


@pytest.mark.asyncio
async def test_vitals_request(aresponses):
    add_valid_vitals_response(aresponses)
    async with aiohttp.ClientSession() as session:
        wall_connector = WallConnector("anyhost", session=session)
        vitals = await wall_connector.async_get_vitals()
        assert vitals.contactor_closed is False
        assert vitals.vehicle_connected is True
        assert vitals.session_s == 0
        assert vitals.grid_v == 228.8
        assert vitals.grid_hz == 50.003
        assert vitals.vehicle_current_a == 0.5
        assert vitals.currentA_a == 0.4
        assert vitals.currentB_a == 0.35
        assert vitals.currentC_a == 0.3
        assert vitals.currentN_a == 0.6
        assert vitals.voltageA_v == 230.1
        assert vitals.voltageB_v == 230.2
        assert vitals.voltageC_v == 230.3
        assert vitals.relay_coil_v == 11.9
        assert vitals.pcba_temp_c == 13.8
        assert vitals.handle_temp_c == 9.9
        assert vitals.mcu_temp_c == 20.8
        assert vitals.uptime_s == 35779
        assert vitals.input_thermopile_uv == -151
        assert vitals.prox_v == 0.01
        assert vitals.pilot_high_v == 11.9
        assert vitals.pilot_low_v == 11.99
        assert vitals.session_energy_wh == 22128.301
        assert vitals.config_status == 5
        assert vitals.evse_state == 1
        assert vitals.current_alerts == ["alert1", "alert2"]
        assert vitals.total_power_w == 241.7


@pytest.mark.asyncio
async def test_lifetime_request(aresponses):
    aresponses.add(
        "anyhost",
        "/api/1/lifetime",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="""
                {
                    "contactor_cycles":175,
                    "contactor_cycles_loaded":3,
                    "alert_count":1603,
                    "thermal_foldbacks":0,
                    "avg_startup_temp":27.8,
                    "charge_starts":175,
                    "energy_wh":386204,
                    "connector_cycles":23,
                    "uptime_s":1945056,
                    "charging_time_s":183022
                }
                """,
        ),
    )

    async with aiohttp.ClientSession() as session:
        wall_connector = WallConnector("anyhost", session=session)
        lifetime = await wall_connector.async_get_lifetime()
        assert lifetime.contactor_cycles == 175
        assert lifetime.contactor_cycles_loaded == 3
        assert lifetime.alert_count == 1603
        assert lifetime.thermal_foldbacks == 0
        assert lifetime.avg_startup_temp == 27.8
        assert lifetime.charge_starts == 175
        assert lifetime.energy_wh == 386204
        assert lifetime.connector_cycles == 23
        assert lifetime.uptime_s == 1945056
        assert lifetime.charging_time_s == 183022


@pytest.mark.asyncio
async def test_version_request(aresponses):
    aresponses.add(
        "anyhost",
        "/api/1/version",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="""
                {
                    "firmware_version":"21.29.1+g4152353e50f744",
                    "part_number":"1529455-02-D",
                    "serial_number":"ACB12345678901"
                }
                """,
        ),
    )

    async with aiohttp.ClientSession() as session:
        wall_connector = WallConnector("anyhost", session=session)
        version = await wall_connector.async_get_version()
        assert version.firmware_version == "21.29.1+g4152353e50f744"
        assert version.part_number == "1529455-02-D"
        assert version.serial_number == "ACB12345678901"


@pytest.mark.asyncio
async def test_internal_session(aresponses):
    add_valid_vitals_response(aresponses)
    async with WallConnector("anyhost") as wall_connector:
        vitals = await wall_connector.async_get_vitals()
        assert vitals.contactor_closed is False


@pytest.mark.asyncio
async def test_timeout(aresponses):
    async def response_handler(_):
        await asyncio.sleep(0.2)
        return get_valid_vitals_response_handler(aresponses)

    # Backoff will try 3 times
    aresponses.add("anyhost", "/api/1/vitals", "GET", response_handler)
    aresponses.add("anyhost", "/api/1/vitals", "GET", response_handler)
    aresponses.add("anyhost", "/api/1/vitals", "GET", response_handler)

    async with aiohttp.ClientSession() as session:
        wall_connector = WallConnector("anyhost", timeout=0.1, session=session)
        with pytest.raises(WallConnectorConnectionTimeoutError):
            assert await wall_connector.async_get_vitals()


@pytest.mark.asyncio
async def test_error_response(aresponses):
    aresponses.add(
        "anyhost",
        "/api/1/vitals",
        "GET",
        aresponses.Response(
            status=500, headers={"Content-Type": "text/plain"}, text="Error"
        ),
    )

    async with aiohttp.ClientSession() as session:
        wall_connector = WallConnector("anyhost", session=session)
        with pytest.raises(WallConnectorConnectionError):
            assert await wall_connector.async_get_vitals()


def get_valid_vitals_response_handler(aresponses):
    return aresponses.Response(
        status=200,
        headers={"Content-Type": "application/json"},
        text="""
            {
                "contactor_closed":false,
                "vehicle_connected":true,
                "session_s":0,
                "grid_v":228.8,
                "grid_hz":50.003,
                "vehicle_current_a":0.5,
                "currentA_a":0.4,
                "currentB_a":0.35,
                "currentC_a":0.3,
                "currentN_a":0.6,
                "voltageA_v":230.1,
                "voltageB_v":230.2,
                "voltageC_v":230.3,
                "relay_coil_v":11.9,
                "pcba_temp_c":13.8,
                "handle_temp_c":9.9,
                "mcu_temp_c":20.8,
                "uptime_s":35779,
                "input_thermopile_uv":-151,
                "prox_v":0.01,
                "pilot_high_v":11.9,
                "pilot_low_v":11.99,
                "session_energy_wh":22128.301,
                "config_status":5,
                "evse_state":1,
                "current_alerts":["alert1","alert2"]
                }
            """,
    )


def add_valid_vitals_response(aresponses):
    aresponses.add(
        "anyhost", "/api/1/vitals", "GET", get_valid_vitals_response_handler(aresponses)
    )


@pytest.mark.asyncio
async def test_can_handle_nan_in_json(aresponses):
    aresponses.add(
        "anyhost",
        "/api/1/lifetime",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="""
                {
                    "contactor_cycles": 450,
                    "contactor_cycles_loaded": nan ,
                    "alert_count":nan,
                    "thermal_foldbacks": 0,
                    "avg_startup_temp": nan,
                    "charge_starts": 450,
                    "energy_wh": 2566837,
                    "connector_cycles": 238,
                    "uptime_s": 15896787,
                    "charging_time_s": 758036
                }
                """,
        ),
    )

    async with aiohttp.ClientSession() as session:
        wall_connector = WallConnector("anyhost", session=session)
        assert await wall_connector.async_get_lifetime()


@pytest.mark.asyncio
async def test_can_handle_missing_end_brace(aresponses):
    aresponses.add(
        "anyhost",
        "/api/1/lifetime",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="""
                {
                    "contactor_cycles": 450,
                    "contactor_cycles_loaded": 3 ,
                    "alert_count":1,
                    "thermal_foldbacks": 0,
                    "avg_startup_temp": 3,
                    "charge_starts": 450,
                    "energy_wh": 2566837,
                    "connector_cycles": 238,
                    "uptime_s": 15896787,
                    "charging_time_s": 758036

                """,
        ),
    )

    async with aiohttp.ClientSession() as session:
        wall_connector = WallConnector("anyhost", session=session)
        assert await wall_connector.async_get_lifetime()


@pytest.mark.asyncio
async def test_can_get_raw_response_from_exception(aresponses):
    fake_response = """
                {
                    "contactor_cycles": 450,
                    "contactor_cycles_loaded": 3 ,
                    "alert_count":1,
                    "thermal_foldbacks": 0,
                    "avg_startup_temp: 3,
                    "charge_starts": 450,
                    "energy_wh": 2566837,
                    "connector_cycles": 238,
                    "uptime_s": 15896787,
                    "charging_time_s": 758036
                    }
                """
    aresponses.add(
        "anyhost",
        "/api/1/lifetime",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=fake_response,
        ),
    )

    async with aiohttp.ClientSession() as session:
        wall_connector = WallConnector("anyhost", session=session)
        try:
            await wall_connector.async_get_lifetime()
        except WallConnectorDecodeError as ex:
            assert ex.get_raw_body() == fake_response
