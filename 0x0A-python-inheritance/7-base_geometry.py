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
