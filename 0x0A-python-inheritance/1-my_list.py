#!/usr/bin/python3
"""
contain MyList class
"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initializing"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
