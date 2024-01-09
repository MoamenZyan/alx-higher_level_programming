#!/usr/bin/python3
"""My class."""


class BaseGeometry:
    """Base Geometry class."""

    def area(self):
        """To calculate the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """To validate the args."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
