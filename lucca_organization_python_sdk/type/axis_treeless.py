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


class RequiredAxisTreeless(TypedDict):
    multilingualName: str

class OptionalAxisTreeless(TypedDict, total=False):
    id: int

    name: str

    url: str

    position: int

    parentAxisId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    isActive: bool

    isReadOnly: bool

    isNNRelation: bool

    level: int

class AxisTreeless(RequiredAxisTreeless, OptionalAxisTreeless):
    pass