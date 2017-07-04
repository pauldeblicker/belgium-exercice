import json


def load(path):
    data = None
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return data


def write(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
