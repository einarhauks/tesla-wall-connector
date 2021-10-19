# Python Tesla Wall Connector API <!-- omit in TOC -->

Python Tesla Wall Connector API for local consumption. This package allows you to monitor your 3rd generation Tesla Wall Connector programmatically. It is mainly created to enable integration with Home Assistant and threfore expoeses an asynchronous API.

## Usage

```python
import asyncio
from tesla_wall_connector import WallConnector
async def main():
    async with WallConnector('TeslaWallConnector_ABC123.localdomain') as wall_connector:
        lifetime = await wall_connector.async_get_lifetime()
        print("energy_wh: {}Wh".format(lifetime.energy_wh))

asyncio.run(main())
```

## Setting up development environment

This Python project is fully managed using the [Poetry][poetry] dependency
manager.

You need at least:

- Python 3.8+
- [Poetry][poetry-install]

To install all packages, including all development requirements:

```bash
poetry install
```

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run the Python tests:

```bash
poetry run pytest
```
