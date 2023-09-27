#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of all side of the square
    """
    def __init__(self, size):
        """Initializes a new square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
