#!/usr/bin/python3
"""a function to check if an object is an instance of a given class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specific class.
    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of obj to.
     """
    if type(obj) is a_class:
        return True
    return False
