#!/usr/bin/python3
"""
this module defines an inherited class-checking
function.
"""


def inherits_from(obj, a_class):
    """checks if an object is an inherited instance
    of a class """
    return issubclass(type(obj), a_class) and type(obj) != a_class
