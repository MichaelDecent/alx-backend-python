import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import (
        Mapping,
        Sequence,
        Any,
        Dict,
        Callable,
        Union
    )


class TestAccessNestedMap(unittest.TestCase):
    """The test fixture for testing the access_nested_map method
    in the utils modules"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            result: Union[Dict, int]) -> None:
        """Test the method access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), result)