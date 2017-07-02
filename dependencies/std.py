import os
import sys

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
