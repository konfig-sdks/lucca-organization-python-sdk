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


class AxisTreeless(BaseModel):
    multilingual_name: str = Field(alias='multilingualName')

    id: typing.Optional[int] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    url: typing.Optional[str] = Field(None, alias='url')

    position: typing.Optional[int] = Field(None, alias='position')

    parent_axis_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='parentAxisId')

    is_active: typing.Optional[bool] = Field(None, alias='isActive')

    is_read_only: typing.Optional[bool] = Field(None, alias='isReadOnly')

    is_n_n_relation: typing.Optional[bool] = Field(None, alias='isNNRelation')

    level: typing.Optional[int] = Field(None, alias='level')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
