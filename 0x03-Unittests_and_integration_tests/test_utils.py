#!/usr/bin/env python3
"""
Unit tests for utils module.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Test access_nested_map raises KeyError with expected message."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_key}'")


class TestMemoize(unittest.TestCase):
    """Test cases for the memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches the result after first call."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)  # First call
            self.assertEqual(obj.a_property, 42)  # Cached call
            mock_method.assert_called_once()      # Ensure a_method called only once


# Optional: If you want the tests to run when file is executed directly
if __name__ == '__main__':
    unittest.main()
