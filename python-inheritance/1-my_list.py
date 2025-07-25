#!/usr/bin/python3
"""
creates Mylist class that
inherits from list.
"""


class MyList(list):
    """Myclass is a sub class of list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))

