#!/usr/bin/python3
"""
this module converts python object 
to Json string.
"""


import json

def to_json_string(my_obj):
    """Return the JSON representation of a Python object"""
    return json.dumps(my_obj)
