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

from lucca_organization_python_sdk.pydantic.user import User

class Department(BaseModel):
    name: str = Field(alias='name')

    code: str = Field(alias='code')

    id: typing.Optional[int] = Field(None, alias='id')

    # Position of the departement in the hierarchical tree
    hierarchy: typing.Optional[str] = Field(None, alias='hierarchy')

    # Position of the parent department in the hierarchical tree
    parent_id: typing.Optional[str] = Field(None, alias='parentId')

    is_active: typing.Optional[bool] = Field(None, alias='isActive')

    # Department's general position in the hierarchy
    position: typing.Optional[int] = Field(None, alias='position')

    # level of the Department. Deduce from Position.
    level: typing.Optional[int] = Field(None, alias='level')

    # Order of the current Department among the children of the Parent Department
    sort_order: typing.Optional[int] = Field(None, alias='sortOrder')

    # ID of the User who is the head of the department
    head_i_d: typing.Optional[int] = Field(None, alias='headID')

    head: typing.Optional[User] = Field(None, alias='head')

    # Users of the department, including inactive users.
    users: typing.Optional[typing.List[User]] = Field(None, alias='users')

    # Only active users of the department
    current_users: typing.Optional[typing.List[User]] = Field(None, alias='currentUsers')

    # Number of active users in the department
    current_users_count: typing.Optional[int] = Field(None, alias='currentUsersCount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
