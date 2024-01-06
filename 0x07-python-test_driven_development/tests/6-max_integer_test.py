#!/usr/bin/python3
"""Unittests for max_integer function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer."""

    def test_ordered(self):
        """Test an order list of integers."""
        order = [1, 5, 7, 10]
        self.assertEqual(max_integer(order), 10)

    def test_unordered(self):
        """Test an unorder list of integers."""
        unorder = [1, 2, 7, 3]
        self.assertEqual(max_integer(unorder), 7)

    def test_begginning(self):
        """Test a list with a beginning value."""
        max_beginning = [8, 4, 3, 1]
        self.assertEqual(max_integer(max_beginning), 8)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        element = [4]
        self.assertEqual(max_integer(element), 4)

    def test_floats(self):
        """Test a list of float."""
        float = [7.47, 5.22, -4.158, 14.7, 5.0]
        self.assertEqual(max_integer(float), 14.7)

    def test_int_floats(self):
        """Test a list of int and float."""
        int_and_float = [2.45, 12.4, -4, 21, 7]
        self.assertEqual(max_integer(int_and_float), 21)

    def test_string(self):
        """Test a string."""
        string = "mariem"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["mariem", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
