#!/usr/bin/python3
"""
Module for reading and printing the content of a file
This module contains a single function called 'read_file'
which opens a file inread mode and prints
its entire content to standard output.
"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents"""
    with open(filename, 'r', encoding='utf-8') as f:
        """ print the content of the dile using .read() function"""
        print(f.read(), end="")
