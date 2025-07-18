#!/usr/bin/python3
"""
Defines a Student class with
JSON filtering.
"""


class Student:
    """Student with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student"""
        if isinstance(attrs, list):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
