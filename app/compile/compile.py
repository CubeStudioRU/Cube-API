import os
from typing import List

from app.objects import CompiledInstanceMod

from app.configuration.config import COMPILED_INSTANCE_FILE, INSTANCE_FILE
from app.objects import CompiledInstance, Instance

from app.compile.modrinth import get_mod_file_from_modrinth
from app.compile.curseforge import get_mod_file_from_curseforge

from app.compile.utils import get_json, save_json

def is_compiled_instance_up_to_date() -> bool | None:
    if not os.path.isfile(COMPILED_INSTANCE_FILE) or not os.path.isfile(INSTANCE_FILE):
        return False
    
    try:
        compiled_instance = CompiledInstance(**get_json(COMPILED_INSTANCE_FILE))
        instance = Instance(**get_json(INSTANCE_FILE))
    except TypeError:
        return None

    if instance.id != compiled_instance.id:
        return False
    
    if instance.version != compiled_instance.version:
        return False
    
    return True

def compile_instance() -> bool:
    if not os.path.isfile(INSTANCE_FILE):
        return False

    instance = Instance(**get_json(INSTANCE_FILE))

    compiled_instance_mods: List[CompiledInstanceMod] = []

    for mod in instance.modrinth:
        instance_mod = get_mod_file_from_modrinth(mod=mod.mod, version=mod.version)
        compiled_instance_mods.append(instance_mod)

    for mod in instance.curseforge:
        instance_mod = get_mod_file_from_curseforge(mod_id=mod.mod_id, file_id=mod.file_id)
        compiled_instance_mods.append(instance_mod)
    
    
    compiled_instance = CompiledInstance(
        id=instance.id,
        name=instance.name,
        version=instance.version,
        changelog=instance.changelog,
        mods=compiled_instance_mods
        )
    
    save_json(compiled_instance.dict(), COMPILED_INSTANCE_FILE)
    return True