#!/usr/bin/env python3
"""
0. Parameterize a unit test
"""
import unittest
from typing import Mapping, Sequence, Any, Dict
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, MagicMock


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

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence):
        """
        Test for exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test for get_json method
    """

    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    @patch('utils.requests')
    def test_get_json(self, test_url: str,
                      expected_result: Dict,
                      mock_requests: MagicMock):
        """
        Get moked json from url
        """
        mock = MagicMock()
        mock.json.return_value = expected_result
        mock_requests.get.return_value = mock
        self.assertEqual(get_json(test_url), expected_result)
