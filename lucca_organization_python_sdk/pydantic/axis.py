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

from lucca_organization_python_sdk.pydantic.axis_treeless import AxisTreeless

Axis = typing.Union[AxisTreeless,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
