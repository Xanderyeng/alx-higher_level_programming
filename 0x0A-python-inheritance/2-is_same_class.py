#!/usr/bin/python3
"""
object is exactly an instance of the specified class
"""

def is_same_class(obj, a_class):
    """
    function that check if an object is an instance of a class
    """
    if not isinstance(a_class, type):
        raise TypeError("obj must be an type of an instance")
    return type(obj) is a_class
