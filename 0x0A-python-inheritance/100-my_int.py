#!/usr/bin/python3
"""
comparation
"""

class MyInt(int):
    """
    class MyInt that inherits from int
    """
    def __eq__(self, num):
        return (int(num) != int(num))

    def __ne__(self, num):
        return (int(num) == int(num))
