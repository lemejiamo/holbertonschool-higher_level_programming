#!/usr/bin/python3
"""
   a function to divide a numbers of
   the matrix, for a specified int
"""


def matrix_divided(matrix, div):
    """
    divide a matrix por div
    """

    # validation of data type
    if type(matrix[0]) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    # analysis size  of list
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[-1]):
            raise TypeError("Each row of the matrix must have the same size")

    # div must be a integer
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    # div must be greater than 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # filling the
    divided_matrix = []

    for i in range(len(matrix)):
        item = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if (round((matrix[i][j] / div), 2)) == 0:
                raise ZeroDivisionError("division by zero")
            item.append(round((matrix[i][j] / div), 2))
        divided_matrix.append(item)

    return divided_matrix
