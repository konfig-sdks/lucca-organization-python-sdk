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


class DepartmentTreeNode(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def node() -> typing.Type['DepartmentTreeNodeNode']:
                return DepartmentTreeNodeNode
            
            
            class children(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DepartmentTreeNode']:
                        return DepartmentTreeNode
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DepartmentTreeNode'], typing.List['DepartmentTreeNode']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'children':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DepartmentTreeNode':
                    return super().__getitem__(i)
            __annotations__ = {
                "node": node,
                "children": children,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["node"]) -> 'DepartmentTreeNodeNode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["children"]) -> MetaOapg.properties.children: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["node", "children", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["node"]) -> typing.Union['DepartmentTreeNodeNode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["children"]) -> typing.Union[MetaOapg.properties.children, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["node", "children", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        node: typing.Union['DepartmentTreeNodeNode', schemas.Unset] = schemas.unset,
        children: typing.Union[MetaOapg.properties.children, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DepartmentTreeNode':
        return super().__new__(
            cls,
            *args,
            node=node,
            children=children,
            _configuration=_configuration,
            **kwargs,
        )

from lucca_organization_python_sdk.model.department_tree_node_node import DepartmentTreeNodeNode
