#!/usr/bin/env python3
"""
This Module contain a unit test for access_nested_map
"""
from utils import access_nested_map, get_json, memoize
from unittest import TestCase, mock
from parameterized import parameterized
from typing import (
        Mapping,
        Sequence,
        Any,
        Dict,
        Callable,
        Union
    )


class TestAccessNestedMap(TestCase):
    """
    This class contain Unit test for a function access_nested_map
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected_result: Union[Dict, int]) -> None:
        """test function for the function access_nested_map()"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError('a')),
            ({"a": 1}, ("a", "b"), KeyError('b')),
        ]
    )
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected_exception: Union[Dict, int]) -> None:
        """
        Test function for exceptions in access_nested_map()
        """

        with self.assertRaises(type(expected_exception)) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(expected_exception))


class TestGetJson(TestCase):
    """
    contains test function for the get_json method
    """
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @mock.patch('utils.requests.get')
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            mock_requests_get: Any) -> None:
        """
        """
        mock_response = mock_requests_get.return_value
        mock_response.json.return_value = test_payload

        self.assertEqual(get_json(test_url), test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """
    constain a test fuction for memorize method in utils module.
    patch.object is used to replace methods of a class instance
    with mock temporarily.
    """
    def test_memoize(self) -> None:
        """Test the memoize function"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock_a_method.assert_called_once()
