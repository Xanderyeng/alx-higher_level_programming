#!/usr/bin/python3
"""
function that writes a string to a text file
"""

def write_file(filename="", text=""):
    """
    function that writes a string to a text file
    """
    with open(filename, mode="w", encoding="utf-8") as the_file:
        return the_file.write(text)
