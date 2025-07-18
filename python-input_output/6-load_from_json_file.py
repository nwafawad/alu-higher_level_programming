#!/usr/bin/python3
"""
this module opens a JSON file, deserializes its contents,
and returns the corresponding Python object.
"""


import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
