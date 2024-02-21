#!/usr/bin/python3
# Author -- Gadoskey
"""This module adds all arguments to a Python list and save them to a file."""

import sys
from os.path import exists

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file

    file_exists = exists("add_item.json")
    if file_exists:
        items = load_from_json_file("add_item.json")
    else:
        items = []
    for arg in sys.argv[1:]:
        items.append(arg)
    save_to_json_file(items, "add_item.json")
