import typing_extensions

from lucca_organization_python_sdk.apis.tags import TagValues
from lucca_organization_python_sdk.apis.tags.axis_sections_api import AxisSectionsApi
from lucca_organization_python_sdk.apis.tags.departments_api import DepartmentsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AXISSECTIONS: AxisSectionsApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AXISSECTIONS: AxisSectionsApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
    }
)
