#!/usr/bin/env python3
"""
A module that contains test classes for client module
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    This test class contains GithubOrgClient test cases
    """
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str,
                 expected_response: Dict,
                 mock_get_json) -> None:
        """
        This method test that GithubOrgClient.org returns the correct value.
        """
        # Set the mock's return value
        mock_get_json.return_value = expected_response
        # Instantiate GithubOrgClient with the org name
        client = GithubOrgClient(org_name)

        # Call the org property, which should trigger a call to get_json
        result = client.org

        # Assert that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/{}"
                                              .format(org_name))
        # Assert that the result matches the expected response
        self.assertEqual(result, expected_response)


if __name__ == '__main__':
    unittest.main()
