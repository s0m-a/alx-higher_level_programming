#!/usr/bin/python3
"""
Defines Rectangle class
"""


class Rectangle:
    """Repre of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints this msg when deleting an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter for the private instance width"""
        return self.__width

    @width.setter
    def width(self, input):
        """setter for the private instance  width"""
        if type(input) is not int:
            raise TypeError("width must be an integer")
        if input < 0:
            raise ValueError("width must be >= 0")
        self.__width = input

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, input):
        """setter for the private instance height"""
        if type(input) is not int:
            raise TypeError("height must be an integer")
        if input < 0:
            raise ValueError("height must be >= 0")
        self.__height = input

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns string repre of rectangle"""
        str = ""
        if self.__width != 0 and self.__height != 0:
            str += "\n".join(str(self.print_symbol) * self.__width
                                for x in range(self.__height))
        return str

    def __repr__(self):
        """returns a str repre of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
