#!/usr/bin/python3
"""
This Module contain a unit test for access_nested_map
"""
from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized, param
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(TestCase):
    """
    This class contain Unit test for a function test_access_nested_map
    """

    @parameterized.expand(
        [
            param(nested_map={"a": 1}, path=("a",), expected_result=1),
            param(nested_map={"a": {"b": 2}}, path=(
                "a",), expected_result={"b": 2}),
            param(nested_map={"a": {"b": 2}}, path=(
                "a", "b"), expected_result=2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected_result: Any
    ) -> Any:
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
