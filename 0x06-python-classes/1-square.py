#!/usr/bin/python3
"""create an empty class called Square"""

class Square:
    """create a square.

    size (no type/value verification)

    atributes:
    size: private instance.
    """

    def __init__(self, size):
        self.__size = size
