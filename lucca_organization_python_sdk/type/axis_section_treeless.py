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


class RequiredAxisSectionTreeless(TypedDict):
    code: str

    multilingualName: str

    axisId: int

class OptionalAxisSectionTreeless(TypedDict, total=False):
    description: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    id: int

    name: str

    url: str

    ownerId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    startOn: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    endOn: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    active: bool

class AxisSectionTreeless(RequiredAxisSectionTreeless, OptionalAxisSectionTreeless):
    pass
