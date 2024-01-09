#!/usr/bin/python3
"""My Class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Child Class."""
    def __init__(self, size):
        """constructor."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """To calculate area of the square."""
        return self.__size ** 2
