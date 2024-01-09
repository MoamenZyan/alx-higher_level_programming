#!/usr/bin/python3
"""My class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Child Class"""
    def __init__(self, width, height):
        """constructor."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """To calculate area and return it."""
        return self.__width * self.__height

    def __str__(self):
        """String representation."""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
