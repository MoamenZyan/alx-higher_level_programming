#!/usr/bin/python3

"""This is my class."""


class Rectangle:
    """Rectangle class.

    Methods:
    __init__: To initialize new instances.
    width: To get or set width.
    Height: To get or set height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize new instances.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """To get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """To set Width.

        Parameters:
        - value (int): New value of width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """To get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """To set the height.

        Parameters:
        - value (int): The new value of height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
