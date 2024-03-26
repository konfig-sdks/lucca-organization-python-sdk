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


class RequiredUser(TypedDict):
    pass

class OptionalUser(TypedDict, total=False):
    id: int

    name: str

    url: str

class User(RequiredUser, OptionalUser):
    pass
