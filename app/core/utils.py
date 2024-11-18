from hashlib import sha256


def hash_dict(data: dict) -> str:
    dict_items = tuple(sorted(data.items()))
    encoded_items = str(dict_items).encode('utf-8')
    hash_object = sha256(encoded_items)

    return hash_object.hexdigest()
