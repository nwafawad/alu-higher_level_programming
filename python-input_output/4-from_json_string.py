#!/usr/bin/python3
"""
this module converts Json string into puthon.
"""


import json


def from_json_string(my_str):
    """Return python object from a Json formatted string."""
    return json.loads(my_str)
