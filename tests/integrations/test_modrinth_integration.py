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


@pytest.mark.asyncio
@pytest.mark.integration
async def test_integration_get_mod_success(modrinth_integration):
    mod = ModrinthMod(mod="sodium", version="mc1.20.4-0.5.8")
    compiled_mod = CompiledInstanceMod(file="sodium-fabric-0.5.8+mc1.20.4.jar",
                                       url="https://cdn.modrinth.com/data/AANobbMI/versions/4GyXKCLd/sodium-fabric-0.5.8%2Bmc1.20.4.jar")

    result = await modrinth_integration.get_mod(mod)

    assert compiled_mod == result


@pytest.mark.asyncio
@pytest.mark.integration
async def test_integration_get_mod_error(modrinth_integration):
    mod = ModrinthMod(mod="ohio-wtf-only", version="mc1.20.4-0.5.8-this-thing-is-not-exists")

    with pytest.raises(Exception, match="is not reachable"):
        await modrinth_integration.get_mod(mod)
