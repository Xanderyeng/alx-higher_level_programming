#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
