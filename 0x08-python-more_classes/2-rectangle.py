#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """Repre of a rectangle"""
    def __init__(self, width=0, height=0):
        """set the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
