import argparse
import os
import re


class FileExist(argparse.Action):
    def __call__(self, parser, namespace, path, option_string=None):
        if not os.path.exists(path):
            raise ValueError(f'{path} doesn\'t exist')
        setattr(namespace, self.dest, path)


class IsISO(argparse.Action):
    def __call__(self, parser, namespace, iso_code, option_string=None):
        if not re.match(r'^[A-Z]{2}-[A-Z]{3}$', iso_code):
            raise ValueError(f'{iso_code} is not a valid ISO 3166-2 code')
        setattr(namespace, self.dest, iso_code)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('src_path', help='Source file path',  type=str, action=FileExist)
    parser.add_argument('iso_code', help='ISO code of the feature', type=str, action=IsISO)
    parser.add_argument('dst_path', help='Destination file path',  type=str, action=FileExist)
    return parser.parse_args()
