""" Simple example showing usage of this library """
# pylint: disable=missing-function-docstring

import asyncio
from tesla_wall_connector import WallConnector


async def main():
    async with WallConnector("TeslaWallConnector_ABC123.localdomain") as wall_connector:
        lifetime = await wall_connector.async_get_lifetime()
        print(f"energy_wh: {lifetime.energy_wh}Wh")


asyncio.run(main())
