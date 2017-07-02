import json
import os
import sys

def get_feature(file_path, feature_id):
    data = get_geojson_data(os.path.join(file_path))

    return [f for f in data['features'] if f['id'] == feature_id][0]

def add_feature(file_path, feature):
    data = get_geojson_data(os.path.join(file_path))

    data['features'].append(feature)
    return data

def get_geojson_data(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        f.close();

    return data;

def write_geojson(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
        f.close

if __name__ == '__main__':
    feature = get_feature(sys.argv[1], int(sys.argv[2]))
    new_provinces = add_feature(sys.argv[3], feature)
    write_geojson(os.path.split(sys.argv[3])[1], new_provinces)
