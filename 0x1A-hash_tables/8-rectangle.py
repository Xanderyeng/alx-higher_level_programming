#!/usr/bin/python3
"""
New subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    new classs rectangle, inhetrance from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
