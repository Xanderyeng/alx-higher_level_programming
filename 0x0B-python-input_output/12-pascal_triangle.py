#!/usr/bin/python3
"""
A Module that draws the Pascals Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given height.

    Args:
        n (int): The height of Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Raises:
        None.

    Note:
        Returns an empty list if n <= 0.
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
