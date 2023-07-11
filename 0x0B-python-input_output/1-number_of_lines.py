#!/usr/bin/python3
"""
Returns the number of lines of a text file
"""

def number_of_lines(filename=""):
    """
    Returns the number of lines of a text file
    """
    with open(filename, encoding="utf-8") as the_file:
        line_count = 0
        while True:
            line = the_file.readline()
            if not line:
                break
            line_count += 1
    return line_count
