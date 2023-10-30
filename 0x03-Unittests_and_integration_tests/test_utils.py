#!/usr/bin/env python3
"""
TestAccessNestedMap module
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """
    Mock HTTP calls module
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        tests that utils.get_json
        returns the expected result
        """
        mock_reponse = Mock()
        mock_reponse.json.return_value = test_payload

        with patch('requests.get', return_value=mock_reponse) as mock_get:
            result = get_json(test_url)
        
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
