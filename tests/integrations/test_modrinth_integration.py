import pytest
from aioresponses import aioresponses

from app.schemas.mod_schema import ModrinthMod, CompiledInstanceMod


@pytest.mark.asyncio
async def test_get_mod_success(modrinth_integration):
    mod = ModrinthMod(mod="mod_id", version="version_id")
    url = f"{modrinth_integration.BASE_URL}/project/{mod.mod}/version/{mod.version}"
    mocked_data = {
        "files": [
            {"primary": True, "filename": "modfile.jar", "url": "http://example.com/modfile.jar"}
        ]
    }

    with aioresponses() as mocked:
        mocked.get(url, payload=mocked_data, status=200)

        result = await modrinth_integration.get_mod(mod)

    assert isinstance(result, CompiledInstanceMod)
    assert result.file == "modfile.jar"
    assert result.url == "http://example.com/modfile.jar"


@pytest.mark.asyncio
async def test_get_mod_no_primary_file(modrinth_integration):
    mod = ModrinthMod(mod="mod_id", version="version_id")
    url = f"{modrinth_integration.BASE_URL}/project/{mod.mod}/version/{mod.version}"
    mocked_data = {
        "files": [
            {"primary": False, "filename": "otherfile.jar", "url": "http://example.com/otherfile.jar"}
        ]
    }

    with aioresponses() as mocked:
        mocked.get(url, payload=mocked_data, status=200)

        result = await modrinth_integration.get_mod(mod)

    assert result is None


@pytest.mark.asyncio
async def test_get_mod_error(modrinth_integration):
    mod = ModrinthMod(mod="mod_id", version="version_id")
    url = f"{modrinth_integration.BASE_URL}/project/{mod.mod}/version/{mod.version}"

    with aioresponses() as mocked:
        mocked.get(url, status=404)

        with pytest.raises(Exception, match="is not reachable"):
            await modrinth_integration.get_mod(mod)


@pytest.mark.asyncio
async def test_extract_mods(modrinth_integration, instance_fixture):
    instance = instance_fixture

    result = await modrinth_integration.extract_mods(instance)

    assert result == instance.modrinth
