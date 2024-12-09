from typing import List

from fastapi.params import Depends

from app.integrations.base_integration import BaseIntegration
from app.integrations.cdn_integration import CdnIntegration, get_cdn_integration
from app.integrations.curseforge_integration import CurseforgeIntegration, get_curseforge_integration
from app.integrations.modrinth_integration import ModrinthIntegration, get_modrinth_integration


async def get_integrations(
        modrinth_integration: ModrinthIntegration = Depends(get_modrinth_integration),
        curseforge_integration: CurseforgeIntegration = Depends(get_curseforge_integration),
        cdn_integration: CdnIntegration = Depends(get_cdn_integration),
) -> List[BaseIntegration]:
    return [
        modrinth_integration,
        curseforge_integration,
        cdn_integration,
    ]
