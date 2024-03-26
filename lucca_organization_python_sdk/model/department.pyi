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


class Department(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Departments, to which users must be attached, are used by the different Lucca solutions for different purposes:

* Define access scopes: for example to restrict the visibility of absences in the Timmi Absences schedule.
* Filtering data in a report: our different reports generally allow to filter data according to the legal entity, the SSC, but also the department of the user.
* Build the organization chart in Poplee Core HR.
The departments are represented as a hierarchical tree with a parent/child relationship.

*NB:* You can have up to 9 levels of departments, and up to 99 departments under a single parent department. However, limiting the number of levels to 7 is recommended.
    """


    class MetaOapg:
        required = {
            "code",
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class code(
                schemas.StrSchema
            ):
                pass
            id = schemas.IntSchema
            hierarchy = schemas.StrSchema
            
            
            class parentId(
                schemas.StrSchema
            ):
                pass
            isActive = schemas.BoolSchema
            
            
            class position(
                schemas.IntSchema
            ):
                pass
            level = schemas.IntSchema
            
            
            class sortOrder(
                schemas.IntSchema
            ):
                pass
            headID = schemas.IntSchema
        
            @staticmethod
            def head() -> typing.Type['User']:
                return User
            
            
            class users(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['User']:
                        return User
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['User'], typing.List['User']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'users':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'User':
                    return super().__getitem__(i)
            
            
            class currentUsers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['User']:
                        return User
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['User'], typing.List['User']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'currentUsers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'User':
                    return super().__getitem__(i)
            
            
            class currentUsersCount(
                schemas.IntSchema
            ):
                pass
            __annotations__ = {
                "name": name,
                "code": code,
                "id": id,
                "hierarchy": hierarchy,
                "parentId": parentId,
                "isActive": isActive,
                "position": position,
                "level": level,
                "sortOrder": sortOrder,
                "headID": headID,
                "head": head,
                "users": users,
                "currentUsers": currentUsers,
                "currentUsersCount": currentUsersCount,
            }
    
    code: MetaOapg.properties.code
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hierarchy"]) -> MetaOapg.properties.hierarchy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentId"]) -> MetaOapg.properties.parentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isActive"]) -> MetaOapg.properties.isActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sortOrder"]) -> MetaOapg.properties.sortOrder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["headID"]) -> MetaOapg.properties.headID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["head"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["users"]) -> MetaOapg.properties.users: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentUsers"]) -> MetaOapg.properties.currentUsers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentUsersCount"]) -> MetaOapg.properties.currentUsersCount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "code", "id", "hierarchy", "parentId", "isActive", "position", "level", "sortOrder", "headID", "head", "users", "currentUsers", "currentUsersCount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hierarchy"]) -> typing.Union[MetaOapg.properties.hierarchy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentId"]) -> typing.Union[MetaOapg.properties.parentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isActive"]) -> typing.Union[MetaOapg.properties.isActive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union[MetaOapg.properties.position, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["level"]) -> typing.Union[MetaOapg.properties.level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sortOrder"]) -> typing.Union[MetaOapg.properties.sortOrder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["headID"]) -> typing.Union[MetaOapg.properties.headID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["head"]) -> typing.Union['User', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["users"]) -> typing.Union[MetaOapg.properties.users, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentUsers"]) -> typing.Union[MetaOapg.properties.currentUsers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentUsersCount"]) -> typing.Union[MetaOapg.properties.currentUsersCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "code", "id", "hierarchy", "parentId", "isActive", "position", "level", "sortOrder", "headID", "head", "users", "currentUsers", "currentUsersCount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hierarchy: typing.Union[MetaOapg.properties.hierarchy, str, schemas.Unset] = schemas.unset,
        parentId: typing.Union[MetaOapg.properties.parentId, str, schemas.Unset] = schemas.unset,
        isActive: typing.Union[MetaOapg.properties.isActive, bool, schemas.Unset] = schemas.unset,
        position: typing.Union[MetaOapg.properties.position, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        level: typing.Union[MetaOapg.properties.level, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sortOrder: typing.Union[MetaOapg.properties.sortOrder, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        headID: typing.Union[MetaOapg.properties.headID, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        head: typing.Union['User', schemas.Unset] = schemas.unset,
        users: typing.Union[MetaOapg.properties.users, list, tuple, schemas.Unset] = schemas.unset,
        currentUsers: typing.Union[MetaOapg.properties.currentUsers, list, tuple, schemas.Unset] = schemas.unset,
        currentUsersCount: typing.Union[MetaOapg.properties.currentUsersCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Department':
        return super().__new__(
            cls,
            *args,
            code=code,
            name=name,
            id=id,
            hierarchy=hierarchy,
            parentId=parentId,
            isActive=isActive,
            position=position,
            level=level,
            sortOrder=sortOrder,
            headID=headID,
            head=head,
            users=users,
            currentUsers=currentUsers,
            currentUsersCount=currentUsersCount,
            _configuration=_configuration,
            **kwargs,
        )

from lucca_organization_python_sdk.model.user import User