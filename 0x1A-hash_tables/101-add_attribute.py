#!/usr/bin/python3
"""
adds a new attribute if is posible
"""
def add_attribute(obj, name, value):
    """
    adds a new atribute if is posible
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
