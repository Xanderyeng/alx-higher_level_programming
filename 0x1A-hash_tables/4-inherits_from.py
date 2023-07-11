#!/usr/bin/python3
"""
object is an instance of, or if the object is an instance of a class that
inherited from, the specified class
"""

def inherits_from(obj, a_class):
    """
    check if object is an instance of or instance of a class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
