#!/usr/bin/env python3
"""
0. Parameterize a unit test
"""
import unittest
from typing import Mapping, Sequence, Any
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for utils
    """

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence,
                               expected_result: Any):
        """
        Parametized test function
        """
        self.assertEqual(access_nested_map(nested_map, path),
                         expected_result)
