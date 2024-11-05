#!/usr/bin/env python3
"""
A module that contains test classes for client module
"""


import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """
        A method to test _public_repos_url
        """
        mock_payload = {
                "repos_url": "https://api.github.com/orgs/test-org/repos"
                }
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_payload

            # Create an instance of GithubOrgClient
            my_class = GithubOrgClient("test-org")

            # Check if _public_repos_url returns the expected repos_url
            expected_url = "https://api.github.com/orgs/test-org/repos"
            self.assertEqual(my_class._public_repos_url, expected_url)


if __name__ == '__main__':
    unittest.main()