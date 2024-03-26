# coding: utf-8

# flake8: noqa

"""
    Organization structure API

    Welcome on the documentation for the Organization Structure API 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: www.lucca.fr
"""

__version__ = "1.0"

# import ApiClient
from lucca_organization_python_sdk.api_client import ApiClient

# import Configuration
from lucca_organization_python_sdk.configuration import Configuration

# import exceptions
from lucca_organization_python_sdk.exceptions import OpenApiException
from lucca_organization_python_sdk.exceptions import ApiAttributeError
from lucca_organization_python_sdk.exceptions import ApiTypeError
from lucca_organization_python_sdk.exceptions import ApiValueError
from lucca_organization_python_sdk.exceptions import ApiKeyError
from lucca_organization_python_sdk.exceptions import ApiException

from lucca_organization_python_sdk.client import LuccaOrganization
