#!/usr/bin/python3

"""This is my function."""


def print_square(size):
    """
    Print squares by size.

    Parameters:
    - size (int): Size of the sqaure.

    Raises:
    - TypeError: If size is not int
    - ValueError: If size smaller than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
