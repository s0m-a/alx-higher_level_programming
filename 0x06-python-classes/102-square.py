#!/usr/bin/python3
"""creating an empty class"""

class Square:
    """
    Represent a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with error handling.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """
        Compare if this square is smaller than another square.

        Args:
            other (Square): The square to compare with.

        Returns:
            bool: True if this square is smaller, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare if this square is smaller or equal to another square.

        Args:
            other (Square): The square to compare with.

        Returns:
            bool: True if this square is smaller or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """
        Compare if this square is equal to another square.

        Args:
            other (Square): The square to compare with.

        Returns:
            bool: True if this square is equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare if this square is not equal to another square.

        Args:
            other (Square): The square to compare with.

        Returns:
            bool: True if this square is not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compare if this square is greater than another square.

        Args:
            other (Square): The square to compare with.

        Returns:
            bool: True if this square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare if this square is greater or equal to another square.

        Args:
            other (Square): The square to compare with.

        Returns:
            bool: True if this square is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

