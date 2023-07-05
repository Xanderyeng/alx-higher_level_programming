#!/usr/bin/python3
"""
Print_square function

Creation Date: July 02, 2023.

Author: Chepkiyeng Alexander.
"""


def print_square(size):
    """
    Function that prints a square with the symbol '#'.

    Arguments:
    size: size of the square.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for h in range(size):
        for w in range(size - 1):
            print('#', end="")
        print('#')
