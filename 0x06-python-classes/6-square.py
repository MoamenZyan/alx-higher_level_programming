#!/usr/bin/python3

"""This module is for square class."""


class Square:
    """this is a square class.

    Attributes:
        __size (int): the size of the square.

    Methods:
        __init__: Initializing new instances.
        area: return are of the square.
        size: is to get the size attribute or to set size.
        my_print: this method prints square by #.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize new instances.

        Args:
            size (int, optional): size of the square, default value is 0.

        Raises:
            TypeError: if size is not integer.
            ValueError: if size is lower than 0.
        """
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

        if isinstance(position, tuple) and len(position) == 2 and isinstance(position[0], int) and isinstance(position[1], int):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Area method is to calculate are of the square.

        Returns:
            int: area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Size method is to get the size attribute.

        Returns:
            int: size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Size method is to set the size attribute.

        Args:
            value (int): is the passed argument to set square size.
        """
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Position method is getting position.

        Returns:
            tuple: returning position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Position method is setting position tuple.

        Args:
            value (tuple): is the new values for position tuple.
        """
        if isinstance(value, tuple) and len(value) == 2 and isinstance(value[0], int) and isinstance(value[1], int):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """My_print method is printing square shape using this # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
