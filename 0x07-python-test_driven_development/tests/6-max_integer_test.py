#!/usr/bin/python3
"""
    unittest to function max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
        TestMax Integer class inherits the unittest module
    """
    def test_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -10, -11, -5]), -1)
        self.assertEqual(max_integer([1, 2, 4, 10e+0]), 10e+0)

    def test_raise_exceptions(self):
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, ['Holberton', 1, 2, 3])
