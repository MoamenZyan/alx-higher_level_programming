#!/usr/bin/python3

"""This is my add integer function."""


def add_integer(a, b=98):
    """
    Add two integers or floats.

    Parameters:
    - a (int or float): The first arg.
    - b (int or float): The second arg.

    Returns:
    - int : The sum of the first and second arg.

    Raises:
    - TypeError: If either a or b is not and int or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
