import json
from pathlib import Path


def get_json(path: Path) -> dict:
    with open(path, 'r') as file:
        return json.load(file)


def save_json(obj: dict, path: Path) -> None:
    with open(path, 'w') as file:
        return json.dump(obj, file)
