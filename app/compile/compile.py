import os
from app.configuration.config import COMPILED_INSTANCE_FILE, INSTANCE_FILE
from app.objects import CompiledInstance, Instance

from app.compile.utils import get_json


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

def compile_instance():
    ...