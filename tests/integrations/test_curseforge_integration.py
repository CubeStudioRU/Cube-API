import pytest
from aioresponses import aioresponses

from app.schemas.integration_schema import CurseforgeMod, CompiledInstanceMod
from tests.conftest import curseforge_integration


@pytest.mark.asyncio
async def test_get_mod_success(curseforge_integration):
    mod = CurseforgeMod(mod="some_mod", mod_id=56354, file_id=12312)
    url = curseforge_integration.BASE_URL + f"/mods/{mod.mod_id}/files/{mod.file_id}"
    mocked_data = {
        "data": {
            "fileName": "modfile.jar",
            "downloadUrl": "http://example.com/modfile.jar",
        }
    }

    with aioresponses() as mocked:
        mocked.get(url, payload=mocked_data, status=200)

        result = await curseforge_integration.get_mod(mod)

    assert isinstance(result, CompiledInstanceMod)
    assert result.file == "modfile.jar"
    assert result.url == "http://example.com/modfile.jar"


@pytest.mark.asyncio
async def test_get_mod_no_data(curseforge_integration):
    mod = CurseforgeMod(mod="some_mod", mod_id=56354, file_id=12312)
    url = curseforge_integration.BASE_URL + f"/mods/{mod.mod_id}/files/{mod.file_id}"
    mocked_data = {"data": {}}

    with aioresponses() as mocked:
        mocked.get(url, payload=mocked_data, status=200)

        with pytest.raises(Exception, match="is empty"):
            result = await curseforge_integration.get_mod(mod)


@pytest.mark.asyncio
async def test_get_mod_error(curseforge_integration):
    mod = CurseforgeMod(mod="another_mod", mod_id=56754, file_id=12332)
    url = curseforge_integration.BASE_URL + f"/mods/{mod.mod_id}/files/{mod.file_id}"

    with aioresponses() as mocked:
        mocked.get(url, status=404)

        with pytest.raises(Exception, match="is not reachable"):
            await curseforge_integration.get_mod(mod)


@pytest.mark.asyncio
async def test_extract_mods(instance_fixture, curseforge_integration):
    instance = instance_fixture

    result = await curseforge_integration.extract_mods(instance)

    assert result == instance.curseforge
