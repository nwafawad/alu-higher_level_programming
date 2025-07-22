#!/usr/bin/python3
"""Square module with area method"""


class Square:
    """Defines a square with size validation"""

    def __init__(self, size=0):
        """Initialize the square with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2
