#!/usr/bin/python3
# Author -- Gadoskey
"""This module defines a JSON file-reading function"""

import json


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file and returns the file"""
    with open(filename) as f:
        return json.load(f)
