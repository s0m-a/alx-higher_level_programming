#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """creating a rectangle"""
    def __init__(self, width=0, height=0):
        """Init the object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Making width private"""
        return self.__width

    @width.setter
    def width(self, value):
        """Handling width errs"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Making height private"""
        return self.__height

    @height.setter
    def height(self, value):
        """Handling height errs"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the  perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """Str repres of rectangle"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        for i in range(self.__height):
            for j in range(self.__width):
                str += '#'
            if i != self.__height - 1:
                str += '\n'
        return str

    def __repr__(self):
        """Repre to develop"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes the object"""
        print("Bye rectangle...")
