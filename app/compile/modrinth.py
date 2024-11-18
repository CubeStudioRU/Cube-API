from requests import request

from app.core.config import BASE_MODRINTH_URL
from app.objects import CompiledInstanceMod


def get_mod_file_from_modrinth(mod: str, version: str) -> CompiledInstanceMod:
    url = BASE_MODRINTH_URL + f'/project/{mod}/version/{version}'
    response = request(method='GET', url=url)
    data = response.json()
    files = data['files']
    for file in files:
        if file['primary'] == True:
            return CompiledInstanceMod(file=file['filename'], url=file['url'])

    return None
