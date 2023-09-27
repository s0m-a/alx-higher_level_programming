#!/usr/bin/python3
"""Creating an empty Class"""


class Square:
    """Defines an square
    Attributes:
        __size (int): Defines square size
        __position (int): Defines gap from edge
    """
    def __init__(self, size=0, position=(0, 0)):
        """inits the square
        Args:
            size (int): Defines the square size
        Returns: None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Takes the size
        Args:
            size (int): Defines the square size
        Returns: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Handle the size errs
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
            size (int): Defines square size
        Returns: size
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Handle the position errs
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
        """ Calculates area of square
        Args:
            size (int): size of the  square
        Returns: Square's area
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square with # charater
        Args:
            size (int): size of the square
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

    def __str__(self):
        """print string """
        if self.size == 0:
            return ("")
        else:
            string = ""
            for num in range(self.__position[1]):
                string += "\n"
            for y in range(self.__size):
                for x in range(self.__size + self.__position[0]):
                    if x < self.__position[0]:
                        string += " "
                    else:
                        string += "#"
                string += "\n"
            string = string[:-1]
            return string
