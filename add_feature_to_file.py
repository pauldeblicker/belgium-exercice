import argparse
import os
import sys

from dependencies import geojson
from dependencies import action

def check_and_format_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('src_path', help='Source file path',  type=str, action=action.FileExist)
    parser.add_argument('iso', help='ISO code of the feature', type=str, action=action.IsISO)
    parser.add_argument('dest_path', help='Destination file path',  type=str, action=action.FileExist)
    parser.parse_args()

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
