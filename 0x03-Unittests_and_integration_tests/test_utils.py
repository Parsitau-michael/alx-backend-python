#!/usr/bin/env python3
"""
This module represents a test class for the utils module
"""


import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    This class houses the test cases for the class method access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, response) -> Any:
        """Method to test acess_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), response)


if __name__ == '__main__':
    unittest.main()
