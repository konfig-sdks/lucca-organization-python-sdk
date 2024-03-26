# coding: utf-8

"""
    Organization structure API

    Welcome on the documentation for the Organization Structure API 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: www.lucca.fr
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from lucca_organization_python_sdk.type.axis_section import AxisSection

class RequiredAxissectionsGetByIdResponse(TypedDict):
    pass

class OptionalAxissectionsGetByIdResponse(TypedDict, total=False):
    data: AxisSection

class AxissectionsGetByIdResponse(RequiredAxissectionsGetByIdResponse, OptionalAxissectionsGetByIdResponse):
    pass
