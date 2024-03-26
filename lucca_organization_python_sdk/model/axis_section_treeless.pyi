# coding: utf-8

"""
    Organization structure API

    Welcome on the documentation for the Organization Structure API 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: www.lucca.fr
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from lucca_organization_python_sdk import schemas  # noqa: F401


class AxisSectionTreeless(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "code",
            "multilingualName",
            "axisId",
        }
        
        class properties:
            code = schemas.StrSchema
            multilingualName = schemas.StrSchema
            axisId = schemas.IntSchema
            description = schemas.AnyTypeSchema
            
            
            class id(
                schemas.IntSchema
            ):
                pass
            name = schemas.StrSchema
            url = schemas.StrSchema
            ownerId = schemas.AnyTypeSchema
            
            
            class startOn(
                schemas.DateTimeBase,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'startOn':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class endOn(
                schemas.DateTimeBase,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'endOn':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            active = schemas.BoolSchema
            __annotations__ = {
                "code": code,
                "multilingualName": multilingualName,
                "axisId": axisId,
                "description": description,
                "id": id,
                "name": name,
                "url": url,
                "ownerId": ownerId,
                "startOn": startOn,
                "endOn": endOn,
                "active": active,
            }
    
    code: MetaOapg.properties.code
    multilingualName: MetaOapg.properties.multilingualName
    axisId: MetaOapg.properties.axisId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multilingualName"]) -> MetaOapg.properties.multilingualName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["axisId"]) -> MetaOapg.properties.axisId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerId"]) -> MetaOapg.properties.ownerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startOn"]) -> MetaOapg.properties.startOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endOn"]) -> MetaOapg.properties.endOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "multilingualName", "axisId", "description", "id", "name", "url", "ownerId", "startOn", "endOn", "active", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multilingualName"]) -> MetaOapg.properties.multilingualName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["axisId"]) -> MetaOapg.properties.axisId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerId"]) -> typing.Union[MetaOapg.properties.ownerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startOn"]) -> typing.Union[MetaOapg.properties.startOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endOn"]) -> typing.Union[MetaOapg.properties.endOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "multilingualName", "axisId", "description", "id", "name", "url", "ownerId", "startOn", "endOn", "active", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, str, ],
        multilingualName: typing.Union[MetaOapg.properties.multilingualName, str, ],
        axisId: typing.Union[MetaOapg.properties.axisId, decimal.Decimal, int, ],
        description: typing.Union[MetaOapg.properties.description, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        ownerId: typing.Union[MetaOapg.properties.ownerId, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        startOn: typing.Union[MetaOapg.properties.startOn, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        endOn: typing.Union[MetaOapg.properties.endOn, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AxisSectionTreeless':
        return super().__new__(
            cls,
            *args,
            code=code,
            multilingualName=multilingualName,
            axisId=axisId,
            description=description,
            id=id,
            name=name,
            url=url,
            ownerId=ownerId,
            startOn=startOn,
            endOn=endOn,
            active=active,
            _configuration=_configuration,
            **kwargs,
        )