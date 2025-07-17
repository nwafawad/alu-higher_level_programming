#!/usr/bin/python3
import json


"""
this module converts python object 
to Json string.
"""
def to_json_string(my_obj):
    """Return the JSON representation of a Python object"""
    return json.dumps(my_obj)
