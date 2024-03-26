# coding: utf-8
"""
    Organization structure API

    Welcome on the documentation for the Organization Structure API 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: www.lucca.fr
"""

import typing
import inspect
from datetime import date, datetime
from lucca_organization_python_sdk.client_custom import ClientCustom
from lucca_organization_python_sdk.configuration import Configuration
from lucca_organization_python_sdk.api_client import ApiClient
from lucca_organization_python_sdk.type_util import copy_signature
from lucca_organization_python_sdk.apis.tags.axis_sections_api import AxisSectionsApi
from lucca_organization_python_sdk.apis.tags.departments_api import DepartmentsApi



class LuccaOrganization(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.axis_sections: AxisSectionsApi = AxisSectionsApi(api_client)
        self.departments: DepartmentsApi = DepartmentsApi(api_client)
