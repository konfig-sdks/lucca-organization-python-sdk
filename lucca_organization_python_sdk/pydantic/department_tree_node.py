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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from lucca_organization_python_sdk.pydantic.department_tree_node_node import DepartmentTreeNodeNode

class DepartmentTreeNode(BaseModel):
    node: typing.Optional[DepartmentTreeNodeNode] = Field(None, alias='node')

    # List of all children departments.
    children: typing.Optional['typing.List["DepartmentTreeNode"]'] = Field(None, alias='children')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
