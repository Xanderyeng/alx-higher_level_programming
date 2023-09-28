#!/usr/bin/python3
"""
function that returns the peak of a list
"""


def find_peak(list_of_integers):
    """
    Find the peak in list_of_integers
    Returns: Peak
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
