#!/usr/bin/python3
"""
New subclass square
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    new classs square, inhetrance from Rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] " + str(self.__size) + "/" + str(self.__size)
