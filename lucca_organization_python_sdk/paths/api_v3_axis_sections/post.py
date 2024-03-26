# coding: utf-8

"""
    Organization structure API

    Welcome on the documentation for the Organization Structure API 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: www.lucca.fr
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from lucca_organization_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from lucca_organization_python_sdk.api_response import AsyncGeneratorResponse
from lucca_organization_python_sdk import api_client, exceptions
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

from lucca_organization_python_sdk.model.axis_section_treeless import AxisSectionTreeless as AxisSectionTreelessSchema
from lucca_organization_python_sdk.model.axis_section import AxisSection as AxisSectionSchema
from lucca_organization_python_sdk.model.axissections_create_new_axis_section_response import AxissectionsCreateNewAxisSectionResponse as AxissectionsCreateNewAxisSectionResponseSchema

from lucca_organization_python_sdk.type.axis_section import AxisSection
from lucca_organization_python_sdk.type.axissections_create_new_axis_section_response import AxissectionsCreateNewAxisSectionResponse
from lucca_organization_python_sdk.type.axis_section_treeless import AxisSectionTreeless

from ...api_client import Dictionary
from lucca_organization_python_sdk.pydantic.axissections_create_new_axis_section_response import AxissectionsCreateNewAxisSectionResponse as AxissectionsCreateNewAxisSectionResponsePydantic
from lucca_organization_python_sdk.pydantic.axis_section_treeless import AxisSectionTreeless as AxisSectionTreelessPydantic
from lucca_organization_python_sdk.pydantic.axis_section import AxisSection as AxisSectionPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = AxisSectionSchema


request_body_axis_section = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'Authorization',
]
SchemaFor200ResponseBodyApplicationJson = AxissectionsCreateNewAxisSectionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AxissectionsCreateNewAxisSectionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AxissectionsCreateNewAxisSectionResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_axis_section_mapped_args(
        self,
        description: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        id: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        multilingual_name: typing.Optional[str] = None,
        owner_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        end_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        active: typing.Optional[bool] = None,
        axis_id: typing.Optional[int] = None,
        parent_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
        children_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if id is not None:
            _body["id"] = id
        if name is not None:
            _body["name"] = name
        if url is not None:
            _body["url"] = url
        if code is not None:
            _body["code"] = code
        if multilingual_name is not None:
            _body["multilingualName"] = multilingual_name
        if owner_id is not None:
            _body["ownerId"] = owner_id
        if start_on is not None:
            _body["startOn"] = start_on
        if end_on is not None:
            _body["endOn"] = end_on
        if active is not None:
            _body["active"] = active
        if axis_id is not None:
            _body["axisId"] = axis_id
        if parent_axis_sections is not None:
            _body["parentAxisSections"] = parent_axis_sections
        if children_axis_sections is not None:
            _body["childrenAxisSections"] = children_axis_sections
        args.body = _body
        return args

    async def _acreate_new_axis_section_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a new AxisSection
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/axisSections',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_axis_section.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_new_axis_section_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a new AxisSection
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/axisSections',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_axis_section.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateNewAxisSectionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_axis_section(
        self,
        description: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        id: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        multilingual_name: typing.Optional[str] = None,
        owner_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        end_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        active: typing.Optional[bool] = None,
        axis_id: typing.Optional[int] = None,
        parent_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
        children_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_axis_section_mapped_args(
            description=description,
            id=id,
            name=name,
            url=url,
            code=code,
            multilingual_name=multilingual_name,
            owner_id=owner_id,
            start_on=start_on,
            end_on=end_on,
            active=active,
            axis_id=axis_id,
            parent_axis_sections=parent_axis_sections,
            children_axis_sections=children_axis_sections,
        )
        return await self._acreate_new_axis_section_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_axis_section(
        self,
        description: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        id: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        multilingual_name: typing.Optional[str] = None,
        owner_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        end_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        active: typing.Optional[bool] = None,
        axis_id: typing.Optional[int] = None,
        parent_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
        children_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_axis_section_mapped_args(
            description=description,
            id=id,
            name=name,
            url=url,
            code=code,
            multilingual_name=multilingual_name,
            owner_id=owner_id,
            start_on=start_on,
            end_on=end_on,
            active=active,
            axis_id=axis_id,
            parent_axis_sections=parent_axis_sections,
            children_axis_sections=children_axis_sections,
        )
        return self._create_new_axis_section_oapg(
            body=args.body,
        )

class CreateNewAxisSection(BaseApi):

    async def acreate_new_axis_section(
        self,
        description: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        id: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        multilingual_name: typing.Optional[str] = None,
        owner_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        end_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        active: typing.Optional[bool] = None,
        axis_id: typing.Optional[int] = None,
        parent_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
        children_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
        validate: bool = False,
        **kwargs,
    ) -> AxissectionsCreateNewAxisSectionResponsePydantic:
        raw_response = await self.raw.acreate_new_axis_section(
            description=description,
            id=id,
            name=name,
            url=url,
            code=code,
            multilingual_name=multilingual_name,
            owner_id=owner_id,
            start_on=start_on,
            end_on=end_on,
            active=active,
            axis_id=axis_id,
            parent_axis_sections=parent_axis_sections,
            children_axis_sections=children_axis_sections,
            **kwargs,
        )
        if validate:
            return AxissectionsCreateNewAxisSectionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AxissectionsCreateNewAxisSectionResponsePydantic, raw_response.body)
    
    
    def create_new_axis_section(
        self,
        description: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        id: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        multilingual_name: typing.Optional[str] = None,
        owner_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        end_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        active: typing.Optional[bool] = None,
        axis_id: typing.Optional[int] = None,
        parent_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
        children_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
        validate: bool = False,
    ) -> AxissectionsCreateNewAxisSectionResponsePydantic:
        raw_response = self.raw.create_new_axis_section(
            description=description,
            id=id,
            name=name,
            url=url,
            code=code,
            multilingual_name=multilingual_name,
            owner_id=owner_id,
            start_on=start_on,
            end_on=end_on,
            active=active,
            axis_id=axis_id,
            parent_axis_sections=parent_axis_sections,
            children_axis_sections=children_axis_sections,
        )
        if validate:
            return AxissectionsCreateNewAxisSectionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AxissectionsCreateNewAxisSectionResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        description: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        id: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        multilingual_name: typing.Optional[str] = None,
        owner_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        end_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        active: typing.Optional[bool] = None,
        axis_id: typing.Optional[int] = None,
        parent_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
        children_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_axis_section_mapped_args(
            description=description,
            id=id,
            name=name,
            url=url,
            code=code,
            multilingual_name=multilingual_name,
            owner_id=owner_id,
            start_on=start_on,
            end_on=end_on,
            active=active,
            axis_id=axis_id,
            parent_axis_sections=parent_axis_sections,
            children_axis_sections=children_axis_sections,
        )
        return await self._acreate_new_axis_section_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        description: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        id: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        multilingual_name: typing.Optional[str] = None,
        owner_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        end_on: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        active: typing.Optional[bool] = None,
        axis_id: typing.Optional[int] = None,
        parent_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
        children_axis_sections: typing.Optional[typing.List[AxisSectionTreeless]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_axis_section_mapped_args(
            description=description,
            id=id,
            name=name,
            url=url,
            code=code,
            multilingual_name=multilingual_name,
            owner_id=owner_id,
            start_on=start_on,
            end_on=end_on,
            active=active,
            axis_id=axis_id,
            parent_axis_sections=parent_axis_sections,
            children_axis_sections=children_axis_sections,
        )
        return self._create_new_axis_section_oapg(
            body=args.body,
        )

