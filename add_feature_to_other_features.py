import json
import os
import sys

def getFeature(filePath, featureId):
    data = getGeojsonData(os.path.join(filePath))

    return [f for f in data['features'] if f['id'] == featureId][0]

def addFeature(filePath, feature):
    data = getGeojsonData(os.path.join(filePath))

    data['features'].append(feature)
    return data

def getGeojsonData(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        f.close();

    return data;

def writeGeojson(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
        f.close

if __name__ == '__main__':
    feature = getFeature(sys.argv[1], int(sys.argv[2]))
    newProvinces = addFeature(sys.argv[3], feature)
    writeGeojson(os.path.split(sys.argv[3])[1], newProvinces)
