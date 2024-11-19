import pytest

from app.integrations.curseforge_integration import CurseforgeIntegration
from app.integrations.modrinth_integration import ModrinthIntegration
from app.schemas.instance_schema import Instance
from app.schemas.mod_schema import ModrinthMod, CurseforgeMod


@pytest.fixture
def curseforge_integration():
    return CurseforgeIntegration()


@pytest.fixture
def modrinth_integration():
    return ModrinthIntegration()


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
            ModrinthMod(mod="laby", version="mc1.20.4-0.2.9")
        ],
        curseforge=[
            CurseforgeMod(mod="structurize", mod_id=5082629, file_id=5082629)
        ]
    )
