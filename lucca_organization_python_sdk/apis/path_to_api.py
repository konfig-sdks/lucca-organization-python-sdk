import typing_extensions

from lucca_organization_python_sdk.paths import PathValues
from lucca_organization_python_sdk.apis.paths.api_v3_axes import ApiV3Axes
from lucca_organization_python_sdk.apis.paths.api_v3_axis_sections import ApiV3AxisSections
from lucca_organization_python_sdk.apis.paths.api_v3_axis_sections_axis_section_id import ApiV3AxisSectionsAxisSectionId
from lucca_organization_python_sdk.apis.paths.api_v3_departments import ApiV3Departments
from lucca_organization_python_sdk.apis.paths.api_v3_departments_tree import ApiV3DepartmentsTree
from lucca_organization_python_sdk.apis.paths.api_v3_departments_department_id import ApiV3DepartmentsDepartmentId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V3_AXES: ApiV3Axes,
        PathValues.API_V3_AXIS_SECTIONS: ApiV3AxisSections,
        PathValues.API_V3_AXIS_SECTIONS_AXIS_SECTION_ID: ApiV3AxisSectionsAxisSectionId,
        PathValues.API_V3_DEPARTMENTS: ApiV3Departments,
        PathValues.API_V3_DEPARTMENTS_TREE: ApiV3DepartmentsTree,
        PathValues.API_V3_DEPARTMENTS_DEPARTMENT_ID: ApiV3DepartmentsDepartmentId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V3_AXES: ApiV3Axes,
        PathValues.API_V3_AXIS_SECTIONS: ApiV3AxisSections,
        PathValues.API_V3_AXIS_SECTIONS_AXIS_SECTION_ID: ApiV3AxisSectionsAxisSectionId,
        PathValues.API_V3_DEPARTMENTS: ApiV3Departments,
        PathValues.API_V3_DEPARTMENTS_TREE: ApiV3DepartmentsTree,
        PathValues.API_V3_DEPARTMENTS_DEPARTMENT_ID: ApiV3DepartmentsDepartmentId,
    }
)
