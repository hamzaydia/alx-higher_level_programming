#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        """Test with multiple elements."""
        self.assertEqual(max_integer([3, 1, 4, 1, 5, 9, 2, 6]), 9)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(max_integer([-4, -2, -8, -1]), -1)

    def test_duplicate_values(self):
        """Test with duplicate values."""
        self.assertEqual(max_integer([4, 4, 4, 4, 5]), 5)

    def test_all_equal_values(self):
        """Test with all equal values."""
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3)

    def test_mixed_type_inputs(self):
        """Test with mixed type inputs."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4])

if __name__ == '__main__':
    unittest.main()
