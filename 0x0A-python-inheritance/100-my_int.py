#!/usr/bin/python3
"""My Class."""


class MyInt(int):
    """rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """To create new instance of the class."""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what is not is now equal"""
        return int(self) != other

    def __ne__(self, other):
        """what is equal is now not"""
        return int(self) == other
