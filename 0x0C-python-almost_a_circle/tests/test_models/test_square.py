#!/usr/bin/python3
"""
Unittest for square.py
Created: July 17, 2023
By: Chepkiyeng Alexander
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    class for testing square.py
    """
    def test_pep8(self):
        """
        testing format of square.py
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
