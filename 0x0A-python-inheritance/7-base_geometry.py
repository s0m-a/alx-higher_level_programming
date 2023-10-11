#!/usr/bin/python3
"""
Contain BaseGeometry Class
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """when called, raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checking if the value is an int and if it's > 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
