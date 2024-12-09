import pytest

from app.integrations.curseforge_integration import CurseforgeIntegration
from app.integrations.modrinth_integration import ModrinthIntegration
from app.schemas.instance_schema import Instance, CompiledInstance
from app.schemas.integration_schema import (
    ModrinthMod,
    CurseforgeMod,
    CompiledInstanceMod,
)


@pytest.fixture
def curseforge_integration():
    return CurseforgeIntegration()


@pytest.fixture
def modrinth_integration():
    return ModrinthIntegration()


@pytest.fixture
def compiled_instance_fixture():
    return CompiledInstance(
        id=0,
        name="CubeShield: Test",
        version="0.0.2",
        changelog="Changelog placeholder",
        instance_hash="c7b53327babb4b3ce5b52fdddd86421c",
        mods=[
            CompiledInstanceMod(file="modfile.jar", url="http://example.com/modfile.jar"),
        ],
    )


@pytest.fixture
def instance_fixture():
    return Instance(
        id=0,
        name="CubeShield: Test",
        version="0.0.2",
        changelog="Changelog placeholder",
        game_version="1.20.1",
        loader="fabric",
        modrinth=[
            ModrinthMod(mod="sodium", version="mc1.20.4-0.5.8"),
            ModrinthMod(mod="capes", version="mc1.20.4-0.6.1"),
            ModrinthMod(mod="laby", version="mc1.20.4-0.2.9"),
        ],
        curseforge=[CurseforgeMod(mod="structurize", mod_id=5082629, file_id=5082629)],
    )
