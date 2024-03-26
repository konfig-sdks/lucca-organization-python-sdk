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

from lucca_organization_python_sdk.type.user import User

class RequiredDepartment(TypedDict):
    name: str

    code: str

class OptionalDepartment(TypedDict, total=False):
    id: int

    # Position of the departement in the hierarchical tree
    hierarchy: str

    # Position of the parent department in the hierarchical tree
    parentId: str

    isActive: bool

    # Department's general position in the hierarchy
    position: int

    # level of the Department. Deduce from Position.
    level: int

    # Order of the current Department among the children of the Parent Department
    sortOrder: int

    # ID of the User who is the head of the department
    headID: int

    head: User

    # Users of the department, including inactive users.
    users: typing.List[User]

    # Only active users of the department
    currentUsers: typing.List[User]

    # Number of active users in the department
    currentUsersCount: int

class Department(RequiredDepartment, OptionalDepartment):
    pass
