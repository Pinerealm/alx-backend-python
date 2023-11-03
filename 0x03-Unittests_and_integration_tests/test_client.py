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
    repos_payload = [{"id": 12345, "node_id": "ertghbjn", "name": "test",
                      "full_name": 'test/test', "private": False,
                      "license": {"key": "apache-2.0", "name": "Apache 2.0"}},
                     {"id": 54321, "node_id": "yuiop", "name": "test2",
                      "full_name": 'test/test2', "private": False,
                      "license": {"key": "mit", "name": "MIT License"}},
                     {"id": 98765, "node_id": "dfghjk", "name": "test3",
                      "full_name": 'test/test3', "private": False,
                      "license": None}]

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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method"""
        mock_get_json.return_value = self.repos_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = self.param["repos_url"]
            test_client = GithubOrgClient("test")
            self.assertEqual(test_client.public_repos(), ["test", "test2",
                                                          "test3"])
            self.assertEqual(test_client.public_repos("apache-2.0"), ["test"])

            self.assertEqual(test_client.public_repos("mit"), ["test2"])
            mock_get_json.assert_called_once_with(self.param["repos_url"])
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""
        test_client = GithubOrgClient("test")
        self.assertEqual(test_client.has_license(repo, license_key), expected)
