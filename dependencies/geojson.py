import json

def get_geojson(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        f.close();

    return data;

def write_geojson(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
        f.close
