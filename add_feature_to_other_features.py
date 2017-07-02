import json
import os
import sys

def check_and_format_args():
    if len(sys.argv) < 4:
        print('Missing arguments (expected at least 2)')
        sys.exit(1)

    file_exist(sys.argv[1])
    sys.argv[2] = convert_integer(sys.argv[2])
    file_exist(sys.argv[3])

def file_exist(file_path):
    if os.path.exists(file_path):
        return

    print(f'{file_path} doesn\'t exist')
    sys.exit(1)

def convert_integer(integer):
    try:
        converted = int(integer)
    except ValueError:
        print(f'{integer} isn\'t an id')
        sys.exit(1)
    else:
        return converted

def get_feature(file_path, feature_id):
    data = get_geojson_data(file_path)

    return [f for f in data['features'] if f['id'] == feature_id][0]

def add_feature(file_path, feature):
    data = get_geojson_data(file_path)

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
    check_and_format_args()
    feature = get_feature(sys.argv[1], sys.argv[2])
    new_provinces = add_feature(sys.argv[3], feature)
    write_geojson(os.path.split(sys.argv[3])[1], new_provinces)
