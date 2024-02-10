
from typing import Dict

from app.objects import CompiledInstanceMod
from app.configuration.config import BASE_CURSEFORGE_URL
from app.configuration.config import CURSEFORGE_API_KEY

from requests import request

def get_mod_file_from_curseforge(mod_id: int, file_id: int) -> CompiledInstanceMod:
    url = BASE_CURSEFORGE_URL + f'/mods/{mod_id}/files/{file_id}'
    response = request(method='GET', url=url, headers={'Accept': 'application/json', 'x-api-key': CURSEFORGE_API_KEY})
    data = response.json()['data']
    return CompiledInstanceMod(file=data['fileName'], url=data['downloadUrl'])