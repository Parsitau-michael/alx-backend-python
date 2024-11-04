#!/usr/bin/env python3
"""
This module represents a test class for the utils module
"""


import unittest
from unittest import mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
from utils import access_nested_map, get_json, memoize


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
                               path: Sequence, response) -> None:
        """Method to test acess_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), response)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """Method to test that a KeyError is raised for above invalid inputs"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A test class for the method get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """A method to test fetching a dict from a url"""
        with mock.patch('requests.get') as MockClass:
            # Mock the requests.get().json() response
            MockClass.return_value.json.return_value = test_payload
            # Call get_json() and assert the result
            result = get_json(test_url)
            self.assertEqual(result, test_payload)

            MockClass.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """A class to test memoization"""
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        instance = TestClass()

        with mock.patch.object(TestClass, 'a_method',
                               return_value=42) as mock_method:
            result1 = instance.a_property
            result2 = instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
