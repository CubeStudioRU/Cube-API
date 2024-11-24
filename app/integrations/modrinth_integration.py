from typing import List

import aiohttp

from app.integrations.base_integration import BaseIntegration
from app.schemas.instance_schema import Instance
from app.schemas.mod_schema import ModrinthMod, CompiledInstanceMod, BaseMod


class ModrinthIntegration(BaseIntegration):
    BASE_URL = "https://api.modrinth.com/v2"

    async def get_mod(self, mod: ModrinthMod) -> CompiledInstanceMod:
        url = self.BASE_URL + f"/project/{mod.mod}/version/{mod.version}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"{self.__repr__()} is not reachable")
                data = await response.json()
                for file in data.get("files", []):
                    if file["primary"]:
                        return CompiledInstanceMod(file=file.get("filename"), url=file.get("url"))
        return None

    async def extract_mods(self, instance: Instance) -> List[BaseMod]:
        return instance.modrinth


modrinth_integration = ModrinthIntegration()
