#!/usr/bin/env python3
"""Test utils.py"""
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """The TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test the access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that a KeyError is raised for the following inputs"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(error.exception))


class TestGetJson(unittest.TestCase):
    """The TestGetJson class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test the get_json method"""
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once()


class TestMemoize(unittest.TestCase):
    """The TestMemoize class
    """
    def test_memoize(self):
        """Test the memoize method"""
        class TestClass:
            """The TestClass class
            """
            def a_method(self):
                """The a_method method
                """
                return 42

            @memoize
            def a_property(self):
                """The a_property method
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once()
