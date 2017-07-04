import os

from . import geojson


def load(file_path, feature_iso):
    for feature in geojson.load(file_path)['features']:
        if feature['properties']['ISO3166-2'] == feature_iso:
            return feature


def append(file_path, feature):
    data = geojson.load(file_path)
    data['features'].append(feature)
    geojson.write(os.path.basename(file_path), data)
