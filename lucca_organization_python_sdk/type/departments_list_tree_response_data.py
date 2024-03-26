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

from lucca_organization_python_sdk.type.department_tree_node import DepartmentTreeNode

class RequiredDepartmentsListTreeResponseData(TypedDict):
    pass

class OptionalDepartmentsListTreeResponseData(TypedDict, total=False):
    # Root department. Always null.
    node: none_type

    # Max depth: 9 levels
    children: typing.List[DepartmentTreeNode]

class DepartmentsListTreeResponseData(RequiredDepartmentsListTreeResponseData, OptionalDepartmentsListTreeResponseData):
    pass
