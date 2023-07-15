#!/usr/bin/python3

"""
Tests for amenity.py module
"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """Unittests for Class Amenity"""
    def setUp(self):
        # self.cmd = HBNBCommand()
        pass

    def tearDown(self):
        # self.cmd = None
        pass


if __name__ == '__main__':
    unittest.main()
