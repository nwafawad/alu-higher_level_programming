#!/usr/bin/python3
"""
this module saves any puthon object into a text file as  Json sting
"""


import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj: The Python object to be serialized.
        filename: The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
