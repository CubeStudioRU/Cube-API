import json
import os


def get_json(path: str) -> dict:
    if os.path.isfile(path):
        with open(path, 'r') as file:
            return json.load(file)


def save_json(obj: dict, path: str) -> None:
    with open(path, 'w') as file:
        return json.dump(obj, file)
