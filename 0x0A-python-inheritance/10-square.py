#!/usr/bin/python3
"""
Contain the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation"""
    def __init__(self, size):
        """instantiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area"""
        return self.__size ** 2
