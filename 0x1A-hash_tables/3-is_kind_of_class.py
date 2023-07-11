#!/usr/bin/python3
"""
object is an instance of, or if the object is an instance of a class that
inherited from, the specified class
"""

def is_kind_of_class(obj, a_class):
    """
    check if object is an instance of or instance of a class.
    """
    return isinstance(obj, a_class)
