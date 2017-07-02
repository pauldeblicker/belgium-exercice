import os
import sys

from dependencies import geojson
from dependencies import check

def check_and_format_args():
    if len(sys.argv) < 4:
        print('Missing arguments (expected at least 2)')
        sys.exit(1)

    check.files_exist(sys.argv[1], sys.argv[3])
    sys.argv[2] = check.convert_integer(sys.argv[2])

def get_feature(file_path, feature_id):
    data = geojson.get_geojson(file_path)

    return [f for f in data['features'] if f['id'] == feature_id][0]

def add_feature(file_path, feature):
    data = geojson.get_geojson(file_path)

    data['features'].append(feature)
    return data

def main():
    check_and_format_args()
    feature = get_feature(sys.argv[1], sys.argv[2])
    new_provinces = add_feature(sys.argv[3], feature)
    geojson.write_geojson(os.path.split(sys.argv[3])[1], new_provinces)

if __name__ == '__main__':
    main()
