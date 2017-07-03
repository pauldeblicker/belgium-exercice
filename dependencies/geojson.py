import json

def get_geojson(path):
    data = None
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_geojson(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
