# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lucca_organization_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V3_AXES = "/api/v3/axes"
    API_V3_AXIS_SECTIONS = "/api/v3/axisSections"
    API_V3_AXIS_SECTIONS_AXIS_SECTION_ID = "/api/v3/axisSections/{axisSectionId}"
    API_V3_DEPARTMENTS = "/api/v3/departments"
    API_V3_DEPARTMENTS_TREE = "/api/v3/departments/tree"
    API_V3_DEPARTMENTS_DEPARTMENT_ID = "/api/v3/departments/{departmentId}"
