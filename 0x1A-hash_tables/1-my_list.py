#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""

class MyList(list):
    """
    class MyList with inheritance from List
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
