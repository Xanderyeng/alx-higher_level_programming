#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for row in matrix:
        squares.append(list(map(lambda x: x**2, row)))
    return squares
