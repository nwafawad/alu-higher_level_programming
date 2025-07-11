#!/usr/bin/python3
"""Square class module"""

class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize square with optional size"""
        self.size = size  # Use the setter here

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square"""
        return self.__size ** 2
