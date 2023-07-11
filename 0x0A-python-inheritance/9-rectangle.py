#!/usr/bin/python3
"""
New class BaseGeometry
"""

class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        function not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function for valideta value
        """
        if type(value) is not int:
            raise TypeError(str(name) + " must be an integer")
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")

class Rectangle(BaseGeometry):
    """
    new classs rectangle, inhetrance from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
