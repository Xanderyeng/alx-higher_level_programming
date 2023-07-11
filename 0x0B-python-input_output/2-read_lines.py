#!/usr/bin/python3
"""
reads n lines of a text file
"""

def read_lines(filename="", nb_lines=0):
    """
    reads n lines of a text file
    """
    with open(filename, encoding="utf-8") as the_file:
        lines = the_file.readlines()
    if nb_lines <= 0 or nb_lines >= len(lines):
        for i in lines:
            print(i, end="")
    else:
        for i in range(nb_lines):
            print(lines[i], end="")
