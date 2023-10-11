#!/usr/bin/python3
"""
Contain the class BaseGeometry
also a subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of the rectangle"""
    def __init__(self, width, height):
        """instantiating"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
