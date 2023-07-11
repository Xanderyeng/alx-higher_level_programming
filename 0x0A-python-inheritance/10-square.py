#!/usr/bin/python3
"""
Imports class Rectangle
"""

from rectangle import Rectangle


"""
Defines class Square
"""


class Square(Rectangle):
    """ Initializes class """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """ Public instance method to calculate area """
    def area(self):
        return self.__size ** 2
