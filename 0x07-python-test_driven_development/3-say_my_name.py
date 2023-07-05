#!/usr/bin/python3
"""
Say my name function.

Creation Date: July 03, 2023.

Author: Chepkiyeng Alexander.
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints 'My name is' and two names.

    Arguments:
    first_name: first name.
    last_name: last name.

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
