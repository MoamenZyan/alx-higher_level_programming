#!/usr/bin/python3

"""This is matrix divided function."""


def matrix_divided(matrix, div):
    """
    Divide matrix elements by div and append it to a new matrix.

    Parameters:
    - matrix (list): The first arg.
    - div (int or float): The second arg.

    Returns:
    - list: A new divided matrix.

    Raises:
    - TypeError: If div is not int or float or one of matrix elements as well.
    - ZeroDivisionError: If div is equal to zero.
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for element in matrix:
        if not isinstance(element, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    matrix_len = len(matrix)
    if matrix_len == 0:
        raise IndexError("List is empty, index out of range")
    row_len = len(matrix[0])
    new_matrix = [[] for _ in range(matrix_len)]
    for i in range(0, matrix_len):
        if row_len != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(0, row_len):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(
                   "matrix must be a matrix (list of lists) of integers/floats"
                    )
            new_matrix[i].append(round(((matrix[i][j]) / div), 2))

    return new_matrix
