import os
import sys

from dependencies import geojson
from dependencies import check

def check_and_format_args():
    if len(sys.argv) < 4:
        print('Missing arguments (expected at least 2)')
        sys.exit(1)

    try:
        check.files_exist(sys.argv[1], sys.argv[3])
    except Exception as error:
        print(error)
        sys.exit(1)

def get_feature(file_path, feature_iso):
    data = geojson.get_geojson(file_path)
    return [f for f in data['features'] if f['properties']['ISO3166-2'] == feature_iso][0]

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
