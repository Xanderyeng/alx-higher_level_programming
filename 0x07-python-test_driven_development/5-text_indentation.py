#!/usr/bin/python3
"""
Text indentation

Creation date: July 03,2023.

Author: Chepkiyeng Alexander.
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of ., ?,:.

    Arguments:
    text: given text.

    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    c = [".", "?", ":"]
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in c:
            print()
            print()
            while text[i + 1] == " ":
                i += 1
        i += 1
