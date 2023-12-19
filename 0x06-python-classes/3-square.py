#!/usr/bin/python3

class Square:
    """this is a square class

    Attributes:
        __size (int): the size of the square
    Methods:
        __init__: Initializing new instances
        area: return are of the square
    """
    def __init__(self, size=0):
        """this method is initializing new instances

        Args:
            size (int, optional): size of the square, default value is 0
        Raises:
            TypeError: if size is not integer
            ValueError: if size is lower than 0
        """
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        """this method is to calculate are of the square
        Returns:
            int: area of the square
        """
        return self.__size ** 2
