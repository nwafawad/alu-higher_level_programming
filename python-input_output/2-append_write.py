#!/usr/bin/python3
"""
This module append text to a file
"""


def append_write(filename="", text=""):
    """this function append text to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
