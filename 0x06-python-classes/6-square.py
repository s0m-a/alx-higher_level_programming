#!/usr/bin/python3
"""Creating an empty Class"""


class Square:
    """Represents a square
    Attributes:
        __size (int): Defines square size
        __position (int): Defines the gap from edge
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialse the square
        Args:
            size (int): Defines size of squares
        Returns: None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Takes the size
        Args:
            size (int): Defines square size
        Returns: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Handle size errs
        Args:
            size (int): square size
        """

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Takes the position
        Args:
            size (int): Defines size of the square
        Returns: size
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Handle the position err
        Args:
            position (int): square offset from margin
        """
        err = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(err)
        else:
            if len(value) != 2:
                raise TypeError(err)
            else:
                for i in range(len(value)):
                    if type(value[i]) is not int:
                        raise TypeError(err)
                    elif value[i] < 0:
                        raise TypeError(err)
            self.__position = value

    def area(self):
        """ Calculates area of the square
        Args:
            size (int): size of a square
        Returns: area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints the  square with # character
        Args:
            size (int): size of square
        """
        if self.__size == 0:
            print('')
        else:
            for line_empty in range(self.__position[1]):
                print('')
            for row in range(self.__size):
                for col in range(self.__size + self.__position[0]):
                    if col < self.__position[0]:
                        print(' ', end='')
                    else:
                        print('#', end='')
                print('')
