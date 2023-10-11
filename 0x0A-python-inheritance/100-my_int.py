#!/usr/bin/python3
"""
Contain MyInt Class
"""


class MyInt(int):
    """rebel version of an int!"""
    def __new__(cls, *args, **kwargs):
        """create a new class instance"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """!= is now =="""
        return int(self) != other

    def __ne__(self, other):
        """== is now !="""
        return int(self) == other
