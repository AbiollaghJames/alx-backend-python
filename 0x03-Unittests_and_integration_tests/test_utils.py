#!/usr/bin/env python3
"""
TestAccessNestedMap module
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class that inherits
    functions to be tested and tests them
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ test function """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
    
    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_result):
        """ tests keyError exception """
        if isinstance(expected_result, Exception):
            with self.assertRaises(expected_result):
                access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
