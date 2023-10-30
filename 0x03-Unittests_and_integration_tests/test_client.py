#!/usr/bin/env python3
"""
TestGithubOrgClient module
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_res):
        """
        test that GithubOrgClient.org
        returns the correct value
        """
        endpoint = f"https://api.github.com/orgs/{org_name}"

        class_instance = GithubOrgClient(org_name)
        class_instance.org()

        mock_res.assert_called_once_with(endpoint)
