#!/usr/bin/python3

class Square:
    """This class is a square class
    Attributes:
        __size (int): the size of the square
    Methods:
        __init__: To initialize a new instances
    """
    def __init__(self, size=0):
        """This Method to initialize a new instances
        Args:
            size (int, optional): the size of the square, Default is 0
        Raises:
            TypeError: if size is not integer
            ValueError: if size is lower than 0
        """
        if type(size) is int and size >= 0:
            self.__size = size
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
