import os
import sys

def files_exist(*paths):
    for path in paths:
        if not os.path.exists(path):
            raise Exception(f'{path} doesn\'t exist')

def convert_integer(integer):
    try:
        return int(integer)
    except ValueError:
        pass
