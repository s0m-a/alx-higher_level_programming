#!/usr/bin/python3
"""
Contain class BaseGeometry
"""


class BaseGeometry:
    """Class with public attribute area"""
    def area(self):
        """raise an exception when it's called"""
        raise Exception("area() is not implemented")
