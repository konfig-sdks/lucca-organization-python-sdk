# coding: utf-8

"""
    Organization structure API

    Welcome on the documentation for the Organization Structure API 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: www.lucca.fr
"""

import unittest
from unittest.mock import patch

import urllib3

import lucca_organization_python_sdk
from lucca_organization_python_sdk.paths.api_v3_axis_sections_axis_section_id import get
from lucca_organization_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV3AxisSectionsAxisSectionId(ApiTestMixin, unittest.TestCase):
    """
    ApiV3AxisSectionsAxisSectionId unit test stubs
        Get an AxisSection by id
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
