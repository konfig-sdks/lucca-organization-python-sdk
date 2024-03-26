# coding: utf-8

"""
    Organization structure API

    Welcome on the documentation for the Organization Structure API 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: www.lucca.fr
"""

import unittest

import os
from pprint import pprint
from lucca_organization_python_sdk import LuccaOrganization

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        luccaorganization = LuccaOrganization(
        
                        authorization = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(luccaorganization)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
