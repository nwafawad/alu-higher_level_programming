#!/usr/bin/python3
"""
defines a Rectangle subclass square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square."""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
