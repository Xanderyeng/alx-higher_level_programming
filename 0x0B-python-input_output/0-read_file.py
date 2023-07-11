#!/usr/bin/python3
"""
print the content of a file
"""

def read_file(filename=""):
    """
    read and print the content of a file
    """
    with open(filename, encoding="utf-8") as the_file:
        print(the_file.read(), end="")
