#!/usr/bin/python3
"""
Unittest for base.py
Created: July 17, 2023
By: Chepkiyeng Alexander
"""
import unittest
import pep8
from models.base import Base



class TestBase(unittest.TestCase):
    """
    class for testing base,py
    """
    def test_pep8(self):
        """
        testing format of base.py
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
