#!/usr/bin/env python3
"""Test client.py"""
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """The TestGithubOrgClient class
    """
    param = {"payload": True,
             "repos_url": "http://test.com"}

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, test_org_name, mock_get_json):
        """Test the org method"""
        mock_get_json.return_value = self.param
        test_client = GithubOrgClient(test_org_name)
        self.assertEqual(test_client.org, self.param)
        self.assertEqual(test_client.org, self.param)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{test_org_name}")

    def test_public_repos_url(self):
        """Test the _public_repos_url method
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = self.param
            test_client = GithubOrgClient("test")
            self.assertEqual(test_client._public_repos_url,
                             self.param["repos_url"])
