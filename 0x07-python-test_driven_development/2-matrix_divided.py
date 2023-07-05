#!/usr/bin/python3
"""
Matrix Divided

Creation Date: July 02, 2023.

Author: Chepkiyeng Alexander.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Arguments:
    matrix: Is the given matrix for apply the div.
    div: Divider.

    Return: A matrix with all results.
    """

    result = []
    if type(matrix) is list:
        if type(div) not in [float, int]:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        prev_row = matrix[0]
        for row in matrix:
            if len(row) != len(prev_row):
                prev_row = row
                raise TypeError("Each row of the matrix must" +
                                " have the same size")
            for elem in row:
                if type(elem) not in [float, int]:
                    raise TypeError("matrix must be a matrix (list of lists)" +
                                    " of integers/floats")
            result.append(list(map(lambda x: round(x/div, 2), row)))
        return result
    raise TypeError("matrix must be a matrix (list of lists)" +
                    " of integers/floats")
