#!/usr/bin/python3
"""
This Module contain a unit test for access_nested_map
"""
from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized, param
from typing import Mapping, Sequence, Union, Dict


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
        self, nested_map: Mapping, path: Sequence, expected_result: Union[Dict, int]
    ) -> None:
        """test function for the function access_nested_map()"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
