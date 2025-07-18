#!/usr/bin/python3
"""
this module Load, add, save
"""


import sys
from os import path

# Import your custom functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try to load existing list
if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add new arguments to the list
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
