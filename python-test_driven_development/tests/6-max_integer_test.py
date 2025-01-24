#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        """Test list of positive integers"""
        self.assertEqual(max_integer([3, 4, 8, 6]), 8)
        self.assertEqual(max_integer([10, 100, 1000, 5000]), 5000)
