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


class RequiredDepartmentsGetAll400Response(TypedDict):
    pass

class OptionalDepartmentsGetAll400Response(TypedDict, total=False):
    Status: int

    Message: str

class DepartmentsGetAll400Response(RequiredDepartmentsGetAll400Response, OptionalDepartmentsGetAll400Response):
    pass
