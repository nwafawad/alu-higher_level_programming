#!/usr/bin/python3
"""
this module contains a class that contains
class-checking function.
"""


def is_kind_of_class(obj, a_class):
    """
    check if an object is an instance or inherited.
    """
    return isinstance(obj, a_class)
