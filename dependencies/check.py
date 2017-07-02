import os
import sys

def files_exist(*paths):
    for path in paths:
        if os.path.exists(path) is False:
            print(f'{path} doesn\'t exist')
            sys.exit(1)

def convert_integer(integer):
    try:
        converted = int(integer)
    except ValueError:
        print(f'{integer} isn\'t an id')
        sys.exit(1)
    else:
        return converted
