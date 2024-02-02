import json
import os
from app.configuration.config import COMPILED_INSTANCE_FILE

def get_json(path: str) -> dict:
    with open(path, 'r') as file:
        return json.load(file)
    
def save_json(obj: dict, path: str) -> None:
    with open(path, 'w') as file:
        return json.dump(obj, file)
    

def get_compiled_instance() -> dict | None:
    if not os.path.isfile(COMPILED_INSTANCE_FILE):
        return None
    
    return get_json(COMPILED_INSTANCE_FILE)