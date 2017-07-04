import argparse
import os
import re
import sys

class FileExist(argparse.Action):
    def __call__(self, parser, namespace, path, option_string=None):
        if not os.path.exists(path):
            raise ValueError(f'{path} doesn\'t exist')

class IsISO(argparse.Action):
    def __call__(self, parser, namespace, iso_code, option_string=None):
        if not re.match(r'^[A-Z]{2}-[A-Z]{3}$', iso_code):
            raise ValueError(f'{iso_code} is not a valid ISO 3166-2 code')
